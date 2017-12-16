# coding: utf-8


class Solution(object):
    """
    026. Remove Duplicates from Sorted Array
    """

    def removeDuplicates(self, nums):
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


nums = [1, 1, 2]
s = Solution()
n = s.removeDuplicates(nums)
print n, nums
