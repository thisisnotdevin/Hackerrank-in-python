class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums = (nums1 + nums2)
        nums.sort()
        l = len(nums)
        h = int(l/2)
        if (l % 2):
            return nums[h]
        else:
            return float(nums[h]+nums[h-1])/2
