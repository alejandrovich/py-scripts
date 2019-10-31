
# given an array of ints in the range 0 to n, 
# where n is the length of the array, find the missing number


class Solution(object):
    def findMissingNumber(self, nums):
        all_numbers = set(range(0, len(nums) + 1))
        return next(
            i for i in
            set(all_numbers).difference(set(nums))
        )

    def findMissing(self, nums):
        all_numbers = {
            i: 0
            for i in range(0, len(nums) + 1)
        }
        for i in nums:
            del all_numbers[i]
        return next(
            i for i in all_numbers
        )



if __name__ == '__main__':
    tests = {
        (0,1,2): 3,
        (1,4,3,2): 0,
    }

    solution = Solution()

    for test, expected in tests.iteritems():
        result = solution.findMissingNumber(test)
        if result != expected:
            print 'Test {}, expected: {}, result: {}'.format(test, expected, result)
        else:
            print 'Success: {} is missing {}'.format(test, result)

    for test, expected in tests.iteritems():
        result = solution.findMissing(test)
        if result != expected:
            print 'Test {}, expected: {}, result: {}'.format(test, expected, result)
        else:
            print 'Success: {} is missing {}'.format(test, result)

