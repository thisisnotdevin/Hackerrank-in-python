class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for i in range(len(nums)-1):
            goal = target - nums[i]
            if goal in nums[i+1:]:
                index = nums.index(goal, i+1)
                return [i, index]
        return []
