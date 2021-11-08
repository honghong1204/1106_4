def win(nums):
    listLength = len(nums)
    curLoc = 0
    PassedIndex = []
    toReturn = []

    count = 0
    while curLoc < (listLength - 1):
        curMaxStepOption = nums[curLoc]
        MaxInOptions = 0
        curMaxLoc = 0
        if curLoc == 0:
            MaxInOptions = curMaxStepOption
        for TryWithinOptions in range(1, curMaxStepOption + 1):
            if curLoc + TryWithinOptions == listLength - 1:  # Meet the last index
                curMaxLoc = listLength - 1
                break
            if nums[curLoc + TryWithinOptions] >= MaxInOptions:  # Try within possibilities and make the greatest one
                MaxInOptions = nums[curLoc + TryWithinOptions]
                curMaxLoc = curLoc + TryWithinOptions
        curLoc = curMaxLoc
        if curMaxLoc == 0:
            curLoc += 1
        else:
            PassedIndex.append(curMaxLoc)
            count += 1
    toReturn.append(count)
    if curLoc == 0:
        PassedIndex.append(curLoc)
    toReturn.append(PassedIndex)
    return toReturn


print(win([1]))
print(win([1, 2, 4, 1, 1, 1]))
print(win([4, 3, 1, 2, 3, 9, 1, 2]))
