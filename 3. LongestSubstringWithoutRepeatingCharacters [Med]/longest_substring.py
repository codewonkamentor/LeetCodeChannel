"""
=========================
APPROACH 1: Brute Force.
1. We use nested loops to generate all possible substrings of the input string.
2. For each substring, we check if it contains all unique characters by comparing its length with the length of its set (which removes duplicates).
3. If a substring with all unique characters is found and it's longer than the current max_length, we update max_length and longest_substring.
4. Finally, we return both the length of the longest substring and the substring itself.

Time - O(n^3)
Space - O(1)
===============
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                sub_str = s[i:j+1]
                sub_str_set = set(sub_str)
                if len(sub_str_set) == len(sub_str):
                    max_length = max(max_length, len(sub_str))
        return max_length


"""
=========================
APPROACH 1: Brute Force.
1. We iterate through the string using enumerate to get both the index and character.
2. If the current character is in last_seen and its last seen position is within the current window, we update start to the next position after the last occurrence.
3. Otherwise, we update max_length if the current window is longer.
4. We always update the last seen position of the current character in char_index.


Time - O(n)
Space - O(n)
===============
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = defaultdict(int)
        start = max_length = 0
        for end, char in enumerate(s):
            if char in seen and start<=seen[char]:
                start = seen[char]+1
            last_seen[char] = end
            max_length = max(max_len, end-start+1)
        return max_length

