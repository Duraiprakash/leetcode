class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0 
        candiate = None
        
        for num in nums:
            if count == 0:
                candiate = num
            if num == candiate:
                count +=1
            else:
                count -= 1
        return candiate