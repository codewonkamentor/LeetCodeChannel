"""
=========================
APPROACH 1: Merge AND Sort Approach

Time - O((m+n)+(m+n)*Log(m+n)), because of computing merged_array and sorting. Here m = len(nums1) & n = len(nums2)
Space - O(m+n), because of storing nums1 & nums2 in merged_array and sorting operation also take same storage. Here m = len(nums1) & n = len(nums2)
=========================
"""
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_array = nums1+nums2 # --> Time: O(m+n), Space: O(m+n)
        sorted_array = sorted(merged_array) # --> Time: O((m+n)*Log(m+n)), Space: O(m+n)
        if len(sorted_array) % 2 == 0:
            mid = len(sorted_array)//2-1
            return (sorted_array[mid]+sorted_array[mid+1])/2
        else:
            mid = len(sorted_array)//2
            return sorted_array[mid]

"""
=========================
APPROACH 2: Merge WITH Sort Approach

Time - O(m+n), because of while loop to iterate both arrays. Here m = len(nums1) & n = len(nums2)
Space - O(m+n), because storing nums1 & nums2 in merged_array. Here m = len(nums1) & n = len(nums2)
=========================
"""
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i, j, merged_array = 0, 0, []
        while i < len(nums1) or j < len(nums2):
            if j >= len(nums2) or (i<len(nums1) and nums1[i] <= nums2[j]):
                merged_array.append(nums1[i])
                i += 1
            else:
                merged_array.append(nums2[j])
                j += 1
        
        if len(merged_array) % 2 == 0:
            mid = len(merged_array)//2-1
            return (merged_array[mid]+merged_array[mid+1])/2
        else:
            mid = len(merged_array)//2
            return merged_array[mid] 

"""
=========================
APPROACH 3: Optimization of Merge With Sort Approach without Merging

Time -  O( ((m+n)/2)+1 ), because of while loop to iterate both arrays. Here m = len(nums1) & n = len(nums2)
Space - O(1), no additional storage. 
=========================
"""
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total_length = len(nums1) + len(nums2)
        target_index = (total_length // 2)+1
        i = j = prev = current = 0
        for count in range(target_index):
            prev = current
            if j >= len(nums2) or (i<len(nums1) and nums1[i] < nums2[j]):
                current = nums1[i]
                i += 1
            else:
                current = nums2[j]
                j += 1
        if total_length%2 == 0:
            return (prev + current) / 2
        else:
            return current

"""
=========================
APPROACH 4: Optimized with Binary Search
    1. Ensure the first array (nums1) is the smaller one.
    2. Perform binary search on the smaller array to find the correct partition.
    3. Calculate the corresponding partition in the larger array.
    4. Compare elements around the partition to determine if it's correct.
    5. Adjust the partition if necessary and repeat until the correct partition is found.

Time -  O(Log(min(m,n))), where m and n are the lengths of the input arrays
Space - O(1), no additional storage. 
=========================
"""
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1)>len(nums2): nums1, nums2 = nums2, nums1
        x, y, = len(nums1), len(nums2)
        low, high = 0, len(nums1)
        half_len = (x+y+1)//2
        while low<=high:
            partition_x = (low+high)//2
            partition_y = half_len-partition_x

            if partition_x == 0: max_left_x = -float("inf")
            else: max_left_x = nums1[partition_x-1]

            if partition_x == x: min_right_x = float("inf")
            else: min_right_x = nums1[partition_x]

            if partition_y == 0: max_left_y = -float("inf")
            else: max_left_y = nums2[partition_y-1]

            if partition_y == y:  min_right_y = float("inf")
            else: min_right_y = nums2[partition_y]

            results = max(max_left_x, max_left_y)
            if max_left_x<=min_right_y and max_left_y<=min_right_x:
                if (x+y)%2 == 1:
                    return results
                else:
                    return (results + min(min_right_x, min_right_y))/2
            elif max_left_x>min_right_y:
                high = partition_x-1
            else:
                low = partition_x+1
