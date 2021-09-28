from typing import List


######################################################################
# Time Complexity: O(N)
# Space Complexity: O(1)
######################################################################
def maxSubArray(nums: List[int]) -> int:
    numsLength = len(nums)
    if numsLength == 1:
        return nums[0]

    bestSumIndex = nums[0]
    ans = bestSumIndex
    for i in range(1, numsLength):
        # Kadane's Algorithm
        bestSumIndex = max(bestSumIndex + nums[i], nums[i])
        ans = max(ans, bestSumIndex)

    return ans
