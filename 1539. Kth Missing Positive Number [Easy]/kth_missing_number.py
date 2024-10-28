"""
1539. Kth Missing Positive Number [Easy]
https://leetcode.com/problems/kth-missing-positive-number
Youtube Video link: https://youtu.be/gAMHlvM03LE

### 1. Question Explanation:
----------------------------
Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.
Return the kth positive integer that is missing from this array.

### 2. Binary Search Solution:
----------------------------
Algorithm Steps:
1. Initialize two pointers:
   - left at the start of the array (index 0)
   - right at the end of the array (index len(arr) - 1)
2. Enter a binary search loop:
   a. Calculate the middle index pivot = (left + right) // 2
   b. Compute the number of missing integers before the pivot element:
        - arr[pivot] - pivot - 1
   c. Compare this number with k:
       - If it's greater than or equal to k, move right to pivot - 1
       - Otherwise, move left to pivot + 1
3. After the loop ends, return k + right + 1 as the kth missing positive integer.


### 3. Complexity Analysis:
----------------------------
Time: O(N)
Space: O(N)

"""
class Solution:
  def findKthPositive(self, arr: List[int], k: int) -> int:
        left, right = 0, len(arr) - 1
        while left <= right:
            pivot = (left + right) // 2
            if arr[pivot] - pivot - 1 >= k:
                right = pivot - 1
            else:
                left = pivot + 1
        return k + right + 1
