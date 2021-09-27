from typing import List

######################################################################
# Time Complexity: O(N)
# Space Complexity: O(1)
######################################################################
def removeDuplicates(nums: List[int]) -> int:
    originalSize = len(nums)
    if originalSize == 0:
        return 0
    
    # Element to compare with Next element
    current = nums[0]
    
    # Index where next unique element to place
    nextIndex = 1
    
    for i in range(1, originalSize):
        # If element different from previous
        # Put it at next index and update variables
        if current != nums[i]:
            nums[nextIndex] = nums[i]        
            current = nums[i]
            nextIndex += 1
        
        # If same as previous continue
        elif current == nums[i]:
            continue
    
    return nextIndex