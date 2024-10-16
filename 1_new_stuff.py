from math import fma
from re import PatternError, compile
from typing import ReadOnly, TypedDict, Protocol, is_protocol


class Point2D(TypedDict):
    x: float
    y: float
    label: ReadOnly[str]


class MyProtocol(Protocol):
    def some_method(self) -> int: ...


def main() -> None:
    print(fma(1.0, 2, 10))

    try:
        compile("[a-")
    except PatternError as e:
        print("e ==>", e)

    point = Point2D(x=1, y=2, label="point object")
    print(f"point={point}")
    point["label"] = "updated point object"  # this gives an error in type checker
    print(f"updated point={point}")
    print(f"protocol Point2D = {is_protocol(Point2D)}")
    print(f"protocol MyProtocoL= {is_protocol(MyProtocol)}")

if __name__ == '__main__':
    main()
