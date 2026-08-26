class Solution(object):
    def twoSum(self, nums, target):
        seen={}
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #By Surendra Patil
        for i,num in enumerate(nums):
            complement = target -num

            if complement in seen:
                return[seen[complement],i]

            seen[num]=i
        