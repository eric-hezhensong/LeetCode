# coding: utf-8


class Solution(object):
    """
    026. Remove Duplicates from Sorted Array
    """

    @staticmethod
    def remove_duplicates(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length == 0:
            return 0

        temp = 0
        i = 1
        while i < length:
            if nums[i] != nums[temp]:
                temp = i
                i += 1
            else:
                nums.pop(i)
                length -= 1

        return length


if __name__ == '__main__':
    solution = Solution()

    nums1 = [1, 1, 2]
    n = solution.remove_duplicates(nums1)
    print n, nums1
