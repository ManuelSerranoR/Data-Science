class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if (len(nums) < 2): return -1
        left = 0
        right = sum(nums[1:])
        if (left == right): return 0
        for i in range(0, len(nums)-1):
            left += nums[i]
            right -= nums[i+1]
            if (left == right): return i+1
        return -1
