"""
https://leetcode.com/problems/random-pick-with-weight/

### 1. Question Explanation:
----------------------------
Given an array w of positive integers, where w[i] describes
the weight of index i, write a function pickIndex which
randomly picks an index in proportion to its weight.

### 2. Solution Explanation:
----------------------------
Create a list of cumulative weights. Choose a random integer
between 1 and the sum of all weights. Binary search the
cumulative list for the index where the random integer
would be inserted and return that index. Probability of
choosing an index is proportional to its weight.

Explanation of why prefixSum works:
Think that if we had an array [1,2,3,4,3]. Normal random pickIndex would pick any index from 0 to 4 with equal probability.
But we want that index=1 is picked by 2/13 probability, index=0 with 1/13 probability and so on. (13 is sum of weights).
To ensure that one way to think of it if we make a larger array (of size 13) where the values are the indices such that index i is repeated w[i] times.
Then if we do a normal rand on this array then index 0 to 12 will be picked randomly with equal probability.
13 index array -> [0, 1,1, 2,2,2, 3,3,3,3, 4,4,4]. So there is a 3/13 chance of picking 2 as 2 is repeated thrice in the new array.
"""

"""
----------------------------------------
### 1. Approach-1: Linear Search Pick Index
----------------------------------------

1. Constructor (__init__):
   - Takes a list of weights w.
   - Constructs a prefix sum array (self.prefix) that contains cumulative sums of the weights, allowing for efficient index selection based on weight.
2. Method (pickIndex):
   - Generates a random target value scaled by the total weight.
   - Iterates through the prefix sums to find the first index where the target is less than or equal to the prefix sum.
   - Returns this index, ensuring that indices with higher weights are more likely to be selected.

----------------------------------------
### 2. Complexity Analysis:
----------------------------------------
Time Complexity:
- O(N) of constructor function for number of weights N.
- O(N) for pickIndex function.

Space Complexity: O(N)
"""
import random

class Solution:
    def __init__(self, w: List[int]):
        self.prefix = []
        prefix_sum = 0
        for weight in w:
            prefix_sum += weight
            self.prefix.append(prefix_sum)

    def pickIndex(self) -> int:
        target = self.prefix[-1] * random.random()
        for i, prefix_sum in enumerate(self.prefix):
            if target <= prefix_sum:
                return i

"""
----------------------------------------
### 1. Approach-2: Binary Search Pick Index
----------------------------------------

1. Constructor (__init__):
   - Takes a list of weights w.
   - Constructs a prefix sum array (self.prefix) that contains cumulative sums of the weights, allowing for efficient index selection based on weight.
2. Method (pickIndex):
   - Generates a random target value scaled by the total weight.
   - Binary Search the target in "prefix_sum"
----------------------------------------
### 2. Complexity Analysis:
----------------------------------------
Time Complexity:
- O(N) of constructor function for number of weights N.
- O(LogN) for pickIndex function.

Space Complexity: O(N)
"""
import random
class Solution:
    def __init__(self, w: List[int]):
        self.prefix = []
        prefix_sum = 0
        for weight in w:
            prefix_sum += weight
            self.prefix.append(prefix_sum)

    def pickIndex(self) -> int:
        target = self.prefix[-1] * random.random()
        low, high = 0, len(self.prefix)
        while low < high:
            mid = low + (high - low) // 2
            if target > self.prefix[mid]:
                low = mid + 1
            else:
                high = mid
        return low
