class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        k=1
        for i in range(1, len(nums)):
            if k<2 or nums[i] != nums[k-2]:
                nums[k] = nums[i]
                k+=1
        return k