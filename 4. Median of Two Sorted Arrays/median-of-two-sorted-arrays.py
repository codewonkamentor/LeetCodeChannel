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
