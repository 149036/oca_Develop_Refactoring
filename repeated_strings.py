import numpy


def repeated_strings(strings: str, horizontal: int, vertical: int):
    """文字列を行と列に繰り返したものを返す

    Args:
        strings (str): 表示する文字列
        horizontal (int): 列方向に文字列を表示する数
        vertical (int): 行方向に文字列を繰り返す数

    Raises:
        Exception: 文字列が 5文字以上 10文字以下 でない場合エラー
        Exception: 文字列に a-zA-Z 以外の物が入っていたらエラー

    Returns:
        str: result, 文字列を行と列に繰り返したもの
    """
    if not (5 <= len(strings) <= 10):
        # TODO: 一時的にprint
        # raise Exception("5文字以上10文字以下")
        print("5文字以上10文字以下")

    for char in strings:
        if not char.isalpha():
            raise Exception("アルファベットのみ")

    result = ""

    for i in range(horizontal):
        result += strings

    for i in range(vertical):
        result += strings + "\n"
    return result


print(
    repeated_strings(
        "sdfasadf", numpy.random.randint(1, 10), numpy.random.randint(1, 10)
    )
)
