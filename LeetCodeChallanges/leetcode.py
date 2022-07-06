from typing import List

def twoSum(nums: List[int], target: int):
    result = []
    if len(nums) == 2:
        result.append(0)
        result.append(1)
    for i in nums:
        for j in nums:
            if nums.index(i) != nums.index(j):
                if i + j == target:
                    result.append(nums.index(i))
                    result.append(nums.index(j))
                    break

        if len(result) == 2:
            break
    return result
print(twoSum([3,2,3], 6))