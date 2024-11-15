class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        new_list = []
        for i in range(len(nums)):
            if nums[i] not in new_list:
                new_list.append(nums.pop(i))
       
        return len(new_list)
        