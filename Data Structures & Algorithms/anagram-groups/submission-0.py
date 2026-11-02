from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dct = defaultdict(list)

        for i in range(len(strs)):
            sorted_s = "".join(sorted(strs[i]))
            dct[sorted_s].append(strs[i])

        return list(dct.values())