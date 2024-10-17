"""
1004. Max Consecutive Ones III [Medium]
https://leetcode.com/problems/random-pick-with-weight/

### 1. Question Explanation:
----------------------------
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

"""

"""
----------------------------------------
### 1. Approach-1: Brute Force: Sliding Window
----------------------------------------
This code implements a brute-force approach to find the longest contiguous subarray of 1s in a binary array while allowing up to k zeros to be flipped:
Outer Loop: Iterates through each possible starting index.
Inner Loop: Expands from each starting index to count zeros and check conditions.
Counting Zeros: If zeros exceed k, it stops checking further for that starting index.
Tracking Maximum Length: Updates and tracks the maximum length found throughout all iterations.

----------------------------------------
### 2. Complexity Analysis:
----------------------------------------
Time Complexity: O(N^2) 
Space Complexity: O(1)
"""
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        max_length = 0
        
        for start in range(n):
            zeros_count = 0
            for end in range(start, n):
                if nums[end] == 0:
                    zeros_count += 1
                
                if zeros_count > k:
                    break
                
                current_length = end - start + 1
                max_length = max(max_length, current_length)
        
        return max_length


"""
----------------------------------------
### 1. Approach-2: Optimal: Sliding Window Optimized
----------------------------------------
This code efficiently implements a sliding window approach to find the longest contiguous subarray of 1s in a binary array while allowing up to k zeros to be flipped:
Sliding Window Technique: Expands and contracts a window defined by indices start and end.
Counting Zeros: Keeps track of zeros within that window and adjusts when exceeding k.
Tracking Maximum Length: Continuously updates and tracks the maximum length found throughout all iterations.

----------------------------------------
### 2. Complexity Analysis:
----------------------------------------
Time Complexity: O(N) 
Space Complexity: O(1)
"""
class Solution:
    def longestOnes(self, nums, k: int) -> int:
        start = count_0 = max_len = 0

        for end in range(len(nums)):
            # Count number of zeros in current window
            if nums[end] == 0:
                count_0 = count_0 + 1

            # If more than k zeros, shrink window from left
            while count_0 > k:
                if nums[start] == 0:
                    count_0 = count_0 - 1
                start += 1

                # Keep track of max_length subarray so far
                max_len = max(max_len, end - start + 1)
        return max_len
