import gc


class Link:
    def __init__(current, next: "Link | None" = None,
                 prev: "Link | None" = None):
        '''current here denotes for self'''
        current.next = next
        if next is not None:
            next.prev = current
        current.prev = prev
        if prev is not None:
            prev.next = current
        current.surprise: "Link | None" = None


def make_chain(depth: int) -> Link:
    '''
    arrow visualization
    0 [None] <- head -> [None]
    1 [None] <- new_head -> [old_head] 
                [None] <- old_head -> [None]
    2 [None] <- new_head -> [old_head] <- old_head -> [old_old_head] 
                [None] <- old_head -> [None]

    3 [None] <- new_head -> [old_head] <- old_old_head -> [old_old_old_head] 
                [None] <- old_head -> [old_old_head] 
                                    [None] <- old_old_head -> [None]

    '''
    head = Link()
    # print("INIT HEAD ==>", head)
    for _i in range(depth):
        # right expression is evaluated first with the older head and head.prev and assigned to 
        head = Link(head, head.prev)
    # while head is not None:
        # print(f"prev={head.prev}, current={head}, next={head.next}")
    #     head = head.next
    return head


G1_THRESHOLD = 4000  # Change these to see the effect
G2_THRESHOLD = 6000  # Change these to see the effect
G3_THRESHOLD = 0

gc.set_threshold(G1_THRESHOLD, G2_THRESHOLD, G3_THRESHOLD)

M = 10_000
N = 5_000


def main() -> None:
    chain = make_chain(M)  # Creates an initial chain with depth M
    count = M  # Initializes count with the depth of the first chain
    next_count = 1_000_000  # Sets the threshold to start checking garbage collection stats

    while True:  # Infinite loop to keep creating new chains and monitoring memory
        newhead = make_chain(N)  # Creates a new chain of depth N
        newhead.prev = chain  # Circular reference: connects the new chain to the previous chain
        count += N  # Increases the count of total nodes created
        if count >= next_count:  # Once the count reaches the next threshold
            # Get the garbage collection counts from the 3 generations of GC
            (g0, g1, g2) = gc.get_count()
            print(f"Current collections: g0::{g0}, g1::{g1}, g2::{g2}")
            (gc0, gc1, gc2) = gc.get_stats()
            print(f"gc0::{gc0}, \ngc1::{gc1},\n gc2::{gc2}")  # Prints detailed garbage collection statistics

            next_count += 1_000_000  # Sets the next threshold for checking GC stats


if __name__ == '__main__':
    main()
