class Solution:
    def productExceptSelf(self, nums):
        prefix_product = [1]
        for i in range(1, len(nums)):
            prefix_product.append(nums[i-1]*prefix_product[-1])
        
        suffix_product = 1
        for i in range(len(nums)-1, -1, -1):
            prod_except_self = prefix_product[i]*suffix_product
            prefix_product[i] = prod_except_self
            suffix_product = suffix_product*nums[i]
        
        return prefix_product
