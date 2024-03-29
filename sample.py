def majorityElement(arr):
    maxItem = max(arr)
    countArr = [0] * (maxItem + 1)

    for i in arr:
        countArr[i] += 1

    for j in range(len(countArr)):
        if countArr[j] > len(arr) // 2:
            return j


# print(majorityElement([3, 2, 3]))


def majorityElement2(nums):
    maxItem = max(nums)
    minItem = min(nums)
    countArr = [0] * (maxItem - minItem + 1)
    res = []

    for i in nums:
        countArr[i] += 1
        print(countArr)

    for j in range(len(countArr)):

        if countArr[j] > len(nums) // 3:
            res.append(j + minItem)

    return res


# print(majorityElement2([-1, -1, -1]))


def findDuplicates(nums):
    i = 0
    res = []

    while i < len(nums):
        correct = nums[i] - 1

        if nums[i] != nums[correct]:
            nums[i], nums[correct] = nums[correct], nums[i]
        else:
            i += 1

    print(nums)

    for i in range(len(nums)):
        if i != nums[i] - 1:
            res.append(nums[i])

    return res


arr = [1, 1, 2]
# print(findDuplicates(arr))


def heightChecker(heights) -> int:
    maxItem = max(heights)
    minItem = min(heights)

    count = [0] * (maxItem + 1)

    for height in heights:
        count[height] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    sortedArr = [0] * len(heights)
    for height in heights[::-1]:
        count[height] -= 1
        sortedArr[count[height]] = height

    print(sortedArr)

    res = 0
    i = 0

    while i < len(heights):
        if sortedArr[i] != heights[i]:
            res += 1
        i += 1

    return res


# print(heightChecker([1, 1, 4, 2, 1, 3]))


def partition(arr, low, high):

    pivot = arr[high]
    j = low - 1

    for i in range(low, high):

        if arr[i] < pivot:
            j += 1
            arr[j], arr[i] = arr[i], arr[j]

    j += 1
    arr[j], arr[high] = arr[high], arr[j]

    return j


def thirdMax(nums, low, high):

    if len(nums) < 3:
        return max(nums)

    thirdMaxValue = len(nums) - 3
    pIndex = partition(nums, low, high)

    if pIndex == thirdMaxValue:
        if nums[pIndex + 1] != nums[pIndex] or nums[pIndex - 1] != nums[pIndex]:
            return nums[pIndex]
        return thirdMax(nums, low, pIndex - 1)

    elif pIndex > thirdMaxValue:
        return thirdMax(nums, low, pIndex - 1)
    else:
        return thirdMax(nums, pIndex + 1, high)


arr = [1, 2, 3, 2]
# print(thirdMax(arr, 0, len(arr) - 1))


def thirdMax2(nums) -> int:

    maxItem = max(nums)

    if len(nums) < 3:
        return max

    count = [0] * (maxItem + 1)

    for i in nums:
        count[i] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    sortedArr = [0] * len(nums)
    for elem in nums[::-1]:
        count[elem] -= 1
        sortedArr[count[elem]] = elem

    itemCount = 0
    j = len(nums) - 1
    duplicate = set()

    while j > 0 and itemCount != 3:

        if sortedArr[j] not in duplicate:
            itemCount += 1
            duplicate.add(sortedArr[j])

        j -= 1

    if itemCount == 3:
        return sortedArr[j]

    return maxItem


print(thirdMax2([3, 2, 1]))


def bitonic(arr, target):
    start = 0
    end = len(arr) - 1

    while start < end:
        mid = (start + end) // 2

        if arr[mid] > target:
            end = mid
        else:
            start = mid + 1

    return start


def counts(teamA, teamB):
    res = []
    teamA.sort()
    print(teamA)
    for score in teamB:

        mid = bitonic(teamA, score)
        print(mid)
        res.append(mid)

    return res


teamA = [2, 3, 10, 5, 4, 8]
teamB = [3, 1, 7, 8]

print(counts(teamA, teamB))
