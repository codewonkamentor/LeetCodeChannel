class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i, n = 0, len(nums)
        while i < n:
            correct_idx = nums[i] - 1 # Correct index of the current value is nums[i] - 1
            # nums[i] != nums[correct_idx] condition is to ignore swapping if the duplicate element is in it's correct index
            if (0 < nums[i] <= n and nums[i] != nums[correct_idx]):  
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i] # Swap the current value to it index
            else:
                i += 1

        for i in range(n):
            if (nums[i]-1 != i):
                return i+1

        return n+1
