class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            current_number = nums[i]
            if i + 1 > len(nums) - 1:
                next_number = 0
            else:
                next_number = nums[i + 1]
                if current_number + next_number == target:
                    
                    return [i, i+1]
