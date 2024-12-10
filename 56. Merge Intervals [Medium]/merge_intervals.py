"""
56. Merge Intervals [Medium]
https://leetcode.com/problems/merge-intervals/


## Algorithm Steps:
---------------------
Step 1: Sorting the Intervals
Step 2: Finding overlap in the intervals
Step 3: If Overlap is found the merge else append interval as is in output array

## Complexity Analysis:
---------------------
Time: O(N)
Space: O(N)
"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        merged_intervals = [intervals[0]]

        for i in range(1, len(intervals)):
            cur_start, cur_end = intervals[i]
            prev_start, prev_end = merged_intervals[-1]

            if prev_end >= cur_start:
                merged_intervals[-1][1] = max(prev_end, cur_end)
            else:
                merged_intervals.append(intervals[i])

        return merged_intervals
    
