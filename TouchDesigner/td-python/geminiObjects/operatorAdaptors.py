import contents

def TOPtoGeminiImagePart(top:TOP) -> contents.GeminiContentImagePart:
	data = top.saveByteArray('.jpeg')
	return contents.GeminiContentImagePart("image/jpeg", data)

def DATtoGeminiTextPart(dat:DAT) -> contents.GeminiContentTextPart:
	input_text = dat.text
	return contents.GeminiContentTextPart(input_text) 

def FIFODattoGeminiTextParts(dat:fifoDAT) -> list[contents.GeminiContentTextPart]:
	input_text = dat.text
	return contents.GeminiContentTextPart(input_text) 
