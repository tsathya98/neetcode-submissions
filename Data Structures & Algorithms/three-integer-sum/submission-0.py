class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        if nums[0] > 0 or len(nums)<3:
            return []
        res = set()
        for i in range(len(nums)-2):
            l, r = i+1, len(nums) - 1
            while l<r:
                cur = nums[i] + nums[l] + nums[r]
                if cur == 0:
                    res.add((nums[i], nums[l], nums[r]))
                    l+=1
                    r-=1
                elif cur > 0:
                    r-=1
                else:
                    l+=1
        return list(list(res))