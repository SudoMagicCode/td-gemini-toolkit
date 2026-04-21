import contents


def TOPtoGeminiImagePart(top: TOP) -> contents.GeminiContentImagePart:
    data = top.saveByteArray(".jpeg")
    return contents.GeminiContentImagePart("image/jpeg", data)


def DATtoGeminiTextPart(dat: DAT) -> contents.GeminiContentTextPart:
    input_text = dat.text
    return contents.GeminiContentTextPart(input_text)


def FIFODattoGeminiContents(fifo: fifoDAT) -> list[contents.GeminiContent]:
    contentList: list[contents.GeminiContent] = []
    for row in fifo.rows():
        rowList = [c.val for c in row]
        nextContent = FifoRowToGeminiContent(rowList)
        contentList.append(nextContent)
    return contentList


# Fiforow is defined as [ROLE, TEXT]


def GeminiContentToFifoRow(content: contents.GeminiOutputContent) -> list[str]:
    role = content.role
    output_text = ""
    for part in content.parts:
        output_text = output_text + part.text + "\n"
    return [role, output_text]


def FifoRowToGeminiContent(row: list[str]) -> contents.GeminiContent:
    role = row[0]
    text = row[1]
    content = contents.GeminiContent(role)
    content.addTextPart(text)
    return content
