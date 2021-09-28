from typing import List


######################################################################
# Time Complexity: O(N)
# Space Complexity: O(1)
######################################################################
def searchInsert(nums: List[int], target: int) -> int:
    numsLength = len(nums)
    if numsLength == 0:
        return 0

    for i in range(numsLength):
        if nums[i] >= target:
            return i

    return numsLength
