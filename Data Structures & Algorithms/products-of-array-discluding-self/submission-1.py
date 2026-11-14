class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        get pref prod and put it in res list
        suffix prod is computed and multiplied with corresponding indices in res
        """
        res = [1]*len(nums)
        pref = 1
        suff = 1
        for i in range(1, len(nums)):
            pref *= nums[i-1]
            res[i] = pref

        for i in range(len(nums)-2, -1, -1):
            suff *= nums[i+1]
            res[i] *= suff
        
        return res
