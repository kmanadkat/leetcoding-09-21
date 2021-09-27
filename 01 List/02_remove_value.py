from typing import List


######################################################################
# Time Complexity: O(N)
# Space Complexity: O(1)
######################################################################
def removeElement(nums: List[int], val: int) -> int:
    length = len(nums)

    # Edge Case
    if length == 0:
        return 0

    currentIndex = 0
    nextIndex = 0

    # Bring currentIndex to first index of Val
    while currentIndex < length and nums[currentIndex] != val:
        currentIndex += 1

    # If currentIndex reached on last index -> val at end
    if currentIndex == length - 1:
        return length - 1

    # Point nextIndex after currentIndex
    nextIndex = currentIndex + 1

    # Compare nextIndex and if == val, swap with currentIndex & update
    # else move nextIndex ahead
    # all val values will be at end of list after loop
    while nextIndex < length:
        if nums[nextIndex] != val:
            nums[currentIndex], nums[nextIndex] = nums[nextIndex], nums[currentIndex]
            currentIndex += 1
            nextIndex += 1
        else:
            nextIndex += 1

    return currentIndex
