def wins(nums):
    listLength = len(nums)
    curLoc = 0
    PassedIndex = []

    count = 0
    while curLoc < (listLength - 1):
        curMaxStepOption = nums[curLoc]
        MaxInOptions = 0
        curMaxLoc = 0
        for TryWithinOptions in range(1, curMaxStepOption + 1):
            if curLoc + TryWithinOptions == listLength - 1:  # Meet the last index
                curMaxLoc = listLength - 1
                break
            if nums[curLoc + TryWithinOptions] >= MaxInOptions:  #Try within possibilities and make the greatest one as the next step
                MaxInOptions = nums[curLoc + TryWithinOptions]
                curMaxLoc = curLoc + TryWithinOptions
        PassedIndex.append(curMaxLoc)
        curLoc = curMaxLoc
        count += 1
    print([count, PassedIndex])


# wins([1, 2, 4, 1, 1, 1])
# wins([4, 3, 1, 2, 3, 9, 1, 2])
