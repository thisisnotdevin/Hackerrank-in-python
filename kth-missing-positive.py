class Solution(object):
    def findKthPositive(self, arr, k):
        left, right = 0, len(arr) - 1
        closest = arr[0]
        while left <= right:
            mid = (left + right) // 2

            if arr[mid] - mid - 1 >= k:
                right = mid - 1
            else:
                left = mid + 1
        
        return left + k
