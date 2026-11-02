from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dct = defaultdict(list)

        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c)-97] += 1
            dct[tuple(count)].append(s)

        return list(dct.values())