"""
=========================
APPROACH 1: Brute Force - Find all substrings

Time - O(n^3), because ...
Space - O(n), because ...
=========================
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_str, max_length = "", 0

        for start in range(len(s)):
            for end in range(start, len(s)):
                left, right = start, end
                while left<=right:
                    if s[left] == s[right]:
                        left, right = left+1, right-1
                    else:
                        break
                else:
                    if end-start+1>max_length:
                        max_length = end-start+1
                        max_str = s[start:end+1]
        return max_str



"""
=========================
APPROACH 2: Expand around center

Time - O(n^2), because ...
Space - O(n), because ...
=========================
"""
class Solution:
    def longestPalindrome(self, s):
        longest  = ""
        
        for idx in range(2*len(s)-1):
            center = idx//2
            left = center
            right = left+(center%2)
            
            while left>= 0 and right<len(s) and s[left] == s[right]:
                left, right = left-1, right+1
            else:
                left, right = left+1, right-1
            
            if right-left+1 > len(longest):
                longest = s[left:right+1]
            
        return longest
