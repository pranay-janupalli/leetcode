"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation."""

class Solution:
    def product_except_self(self, nums: List[int]) -> List[int]:
        n=len(nums)
        answer=[1]*n
        left_prod=1
        for i in range(len(nums)):
            answer[i]=left_prod
            left_prod*=nums[i]
        right_prod=1
        for j in range(len(nums)-1,-1,-1):
            answer[j]*=right_prod
            right_prod*=nums[j]
        return answer
arr=[1,2,3,4]
print(Solution().product_except_self(arr)) #[24,12,8,6]
