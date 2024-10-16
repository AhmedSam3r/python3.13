from dataclasses import dataclass
import sys


@dataclass
class Node:
    value: int
    next: "Node | None" = None
    prev: "Node | None" = None


def main():
    # creating two nodes
    node1 = Node(10)
    # the count will be +1, since the gc list refers to the object, too
    # Why the Count is +1: When you call sys.getrefcount(node1), 
    # the function receives node1 as an argument. This action itself creates a temporary reference to the object within the function,
    #  which temporarily increases its reference count by 1. 
    # As a result, the reference count returned is incremented by 1 compared to what you would expect from references outside the function.
    print(f"node1 count={sys.getrefcount(node1)}")
    node2 = Node(20)
    print(f"node1 count={sys.getrefcount(node2)}")

    # creating a circular reference
    node1.next = node2
    node2.prev = node1
    print(f"node1 count={sys.getrefcount(node2)}")
    print(f"node2 count={sys.getrefcount(node2)}")

    # creating a circular references between node1 and node2
    node2.next = node1
    node1.prev = node2
    print(f"node1 count={sys.getrefcount(node2)}")
    print(f"node2 count={sys.getrefcount(node2)}")

    # del references
    # references counting won't work in this case
    # cyclic garbage comes into play
    del node1
    del node2
    # gives an error
    # UnboundLocalError: cannot access local variable 'node1' where it is not associated with a value
    # print(f"node1 count={sys.getrefcount(node1)}")
    # print(f"node2 count={sys.getrefcount(node2)}")


if __name__ == '__main__':
    main()
