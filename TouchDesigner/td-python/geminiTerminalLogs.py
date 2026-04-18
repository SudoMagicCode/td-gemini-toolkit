from datetime import datetime


# NOTE gemini generated function
def get_pretty_timestamp():
    """Returns the current time formatted as YYYY-MM-DD | HH:MM:SS"""
    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S |")


def msg_formatter(msg: str, indent: int = 0, displayInTextport: bool = True) -> str:
    """Prints and returns a string with a time stamp and indent - suitable for logs
    and the textport
    """
    indentText = f"{'--' * indent}> "
    formattedMsg = f"{get_pretty_timestamp()} ❇️ {indentText if indent>0 else ''}{msg}"
    if displayInTextport:
        print(formattedMsg)
    return formattedMsg
