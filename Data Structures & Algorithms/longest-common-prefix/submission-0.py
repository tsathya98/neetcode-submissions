class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        '''
        Intuition
            pref = strs[0]
            iterate from 1:len(strs)
                check if strs[i] is starting with pref
                    if not pref = pref[:-1]
        '''
        pref = strs[0]
        for i in range(1, len(strs)):
            while not strs[i].startswith(pref):
                pref = pref[:-1]
        return pref