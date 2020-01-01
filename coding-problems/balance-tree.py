def _describe():
    print(
        '######################################33333\n'
        'Finding the midpoint of a list of integers\n'
        'Taken from a somewhere I cannot remember.\n'
        '######################################33333\n'
    )

tests = (
    ([], None, 'List with no items has no balance'),
    ([1, 1], 0, 'Midpoint of two identical items is 0.'),
    ([2, 2], 0, 'Midpoint of two identical items is 0.'),
    ([1, 1, 1, 1], 1, 'Midpoint of four identical items is 1.'),
    ([2, 1, 1], 0, 'Midpoint of 2,1,1 is 0.'),
    ([1, 1, 2], 1, 'Midpoint of 1,1,2 is 1.'),
    ([1, 1, 1, 1, 1, 2], 2, 'Midpoint of [1, 1, 1, 1, 1, 2] is 2.'),
    ([5, 1, 2, 2, 2, 1, 2], 2, 'Midpoint of [5, 1, 2, 2, 2, 1, 2] is 2.'),
)

def get_midpoint(size):
    mid = size / 2

    # if mid > 0:
    #     mid -= 1

    return mid


def slice_tree(size):
    # size is even
    if size % 2 == 0:
        return size / 2
    else:
        return size / 2



def balance_tree(a):
    '''
    List with one node is balanced at index 0
    List [1, 1] is balanced at 0 (i.e. all elements up to the index)
    List with 0 elements is an error
    '''
    if not a:
        return None

    best = -1
    slice_point = -1
    counter = 0

    print 'slicing a{}'.format(a)
    # inclusive indexes of bounds under consideration each loop
    left_bound = 0
    right_bound = len(a)
    mid = max((get_midpoint(right_bound - left_bound) - 1, 0))

    if len(a) == 1:
        return 0

    while counter < 4:
        left = a[0:mid + 1]
        right = a[mid + 1:]
        print 'now considering a{} to a{}, bounds({},{})'.format(
            left,
            right,
            left_bound,
            right_bound,
        )

        sleft = sum(left)
        sright = sum(right)
        if sleft == sright:
            return mid
        else:
            result = max((sleft, sright))
            if result < best or best < 0:
                best = result
                slice_point = mid
                print 'set best to {}, slicing {}'.format(best, slice_point)

            # adjust these bounds
            if sleft > sright:
                print 'Left is bigger'
                print 'Updating right bound from {} to {}'.format(
                    right_bound, mid
                )
                right_bound = mid
            else:
                print 'Right is bigger'
                print 'Updating left bound from {} to {}'.format(
                    left_bound, mid + 1
                )
                left_bound = mid + 1


            # if there's no more room to slice between the bounds, return
            if right_bound <= left_bound + 1:
                print 'No more room to slice, last: {}'.format(slice_point)
                return slice_point

            mid = left_bound + max(
                (get_midpoint(right_bound - left_bound) - 1, 0)
            )
            print 'New mid at {}'.format(mid)

        counter += 1


def run_tests():
    for test in tests:
        result = balance_tree(test[0])
        print result == test[1], test[2]
        print 


if __name__ == '__main__':
    _describe()
    run_tests()
