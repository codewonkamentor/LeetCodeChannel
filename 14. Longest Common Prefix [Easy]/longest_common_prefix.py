"""
14. Longest Common Prefix [Easy]
https://leetcode.com/problems/longest-common-prefix
Youtube Video link: https://youtu.be/cm62IbA0vG4

### 1. Question Explanation:
----------------------------
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".


### 2. Character Comparison Solution:
----------------------------
Algorithm Steps:
1. Initialization: Start with an empty results list and set character index to zero.
2. Character Comparison: For each character index, compare that character across all strings.
3. Mismatch Handling: If a mismatch is found or if one string ends, return the collected characters as the longest common prefix.
4. Completion: If all characters match up to the length of the shortest string, return those characters as the result.

### 3. Complexity Analysis:
----------------------------
Total Time: O(M*N), where “N” is the number of strings and “M” is the length of the shortest string
Total Space: O(M), where  “M” is the length of the shortest string

"""


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        results, char_idx = [], 0

        while char_idx<len(strs[0]):
            #Character to compare
            char = strs[0][char_idx]
            for i in range(1, len(strs)):
                if char_idx==len(strs[i]) or strs[i][char_idx] != char:
                    return "".join(results)
            results.append(char)
            char_idx += 1
        return "".join(results)
