class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Greedy approach
        if len(nums) == 0:
            return 1
        max_ele = nums[0]
        count = 0
        for num in nums:
            if count == 0:
                max_ele = num
            if num == max_ele:
                count+=1
            else:
                count-=1
        return max_ele