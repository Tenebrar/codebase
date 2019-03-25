from typing import Any, NoReturn, Optional, Union


def do_the_thing(a: Union[str, bytes], b: Optional[int], c: Any) -> NoReturn:
    # Union[str, bytes] may be replaced with AnyStr

    print(a)
    while True:
        if b:
            raise Exception(c)
