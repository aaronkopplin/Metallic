def stringToBytes(string: str, numBytes: int) -> str:
    hexValues = "0x"

    #convert chars to utf-8 digits
    for char in string:
        hexValues += char.encode().hex()

    # pad the end of the string with 0x00
    for i in range(numBytes - len(string)):
        hexValues += "00"

    return hexValues