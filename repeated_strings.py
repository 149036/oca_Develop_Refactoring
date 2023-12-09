def repeated_strings(strings: str, horizontal: int, vertical: int):
    if not (5 <= len(strings) <= 10):
        raise Exception("5文字以上10文字以下")

    for char in strings:
        if not char.isalpha():
            raise Exception("アルファベットのみ")

    result = ""

    for i in range(horizontal):
        result += strings

    for i in range(vertical):
        result += strings + "\n"

    return result


print(repeated_strings("sdfasadf", 5, 5))
