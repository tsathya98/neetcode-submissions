class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        j = 0
        max_sub = 0
        for i in range(len(s)):
            while s[i] in seen:
                seen.discard(s[j])
                j+=1
            seen.add(s[i])
            max_sub = max(max_sub, len(seen))
        return max_sub
