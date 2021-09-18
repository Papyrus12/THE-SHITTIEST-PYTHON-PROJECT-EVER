"""
    trynna make this retarded but i had to actually be retarded to make it so
    this is not truly retarded what a scam
    - FireRedz
"""

""" Declarations """
from PIL.Image import init


IS_RUNABLE: bool = False
""" End of declarations """


def make_sure_is_runnable() -> None:
    global IS_RUNABLE
    IS_RUNABLE = True


def check_if_runnable_is_actually_runnable() -> None:
    global IS_RUNABLE

    if not IS_RUNABLE:
        raise Exception("Checks failed on `check_if_runnable_is_actually_runnable`.")
    else:
        print("[Checks] `check_if_runnable_is_actually_runnable` Passed!")


REAL_PRINT = print


def print(t: str, reverse: bool = False) -> None:
    if reverse:
        REAL_PRINT(t[::-1])
    elif not reverse:
        REAL_PRINT(t)
    else:
        raise Exception("Invalid reverse argument!")


def safe_print(t: str, prefix: str = None) -> None:
    check_if_runnable_is_actually_runnable()

    try:
        if prefix:
            t = prefix + t
    except:
        raise Exception("[SafePrint] Invalid prefix")

    try:
        print(t)
    except:
        raise Exception("[SafePrint] Failed to safely print.")


def make_runnable_not_runnable() -> None:
    global IS_RUNABLE
    IS_RUNABLE = False


def initialize_file() -> None:
    make_sure_is_runnable()
    check_if_runnable_is_actually_runnable()


def close_file() -> None:
    make_runnable_not_runnable()


if __name__ == "__main__":
    raise Exception("You cant run this file directly, import it somewhere else.")
elif __name__ != "__main__":
    initialize_file()
