from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        # If the array is not rotated (already sorted)
        if nums[left] <= nums[right]:
            return nums[left]

        while left < right:
            mid = (left + right) // 2

            # Minimum is in the right half if mid element > right element
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                # Minimum is in the left half including mid
                right = mid

        # left == right -> index of minimum
        return nums[left]
