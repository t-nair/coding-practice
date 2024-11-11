# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

class Solution:
    def two_sum(self, nums:List[int], target:int) -> List[int]:
        answer = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    answer.append(i)
                    answer.append(j)
                    return answer


# using a hashmap
    def faster_two_sum(self, nums:List[int], target:int) -> List[int]:
        pair_indexes = {}

        for i, num in enumerate(nums):
            c = target-num
            if c in pair_indexes:
                return [i, pair_indexes[c]]
            pair_indexes[num] = i
            

