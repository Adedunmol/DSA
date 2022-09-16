import collections


def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_item = list[mid]

        if mid_item == item:
            return mid
        if mid_item < item:
            low = mid + 1
        else:
            high = mid - 1
    return None


my_list = [1, 3, 5, 7, 9]

# print(binary_search(my_list, 3))
# print(binary_search(my_list, -1))


my_list2 = [15, 16, 19, 20, 25, 26, 3, 4, 5, 7, 10, 14]


def binary_search_rotated(list, target):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]

        if guess == target:
            return mid

        if guess < list[high]:  # if that portion is sorted

            if (
                target < list[high]
            ):  # if the number we are looking for is less than the highest element

                if (
                    guess > target
                ):  # if guess is greater than target, it is not in the right portion
                    high = mid - 1
                else:
                    low = mid + 1

            elif target == list[high]:
                low = mid + 1

            else:
                high = mid - 1

        else:  # that portion is not sorted

            if (
                target > list[high]
            ):  # if number we are looking for is greater than highest element

                if (
                    target > guess
                ):  # if target is greater than guess, target is going to be in the right half
                    low = mid + 1
                else:
                    high = mid - 1

            else:
                low = mid + 1

    return None


# print(binary_search_rotated(my_list2, 14))


def minimum_rotated_sorted(list):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]

        if low == high:
            return list[mid]

        if guess < list[high]:
            high = mid
        else:
            low = mid + 1

    return None


# print(minimum_rotated_sorted(my_list2))

# return index of smallest number >= target
def ceiling(arr, target):

    # what if target is greater than greatest number in the array
    if target > arr[len(arr) - 1]:
        return -1

    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2
        guess = arr[mid]

        if target == guess:
            return mid
        elif guess < target:
            start = mid + 1
        else:
            end = mid - 1

    return start


arr = [2, 3, 5, 9, 14, 16, 18]
# print(ceiling(arr, 19))

# return index of greatest number <= target
def floor(arr, target):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2
        guess = arr[mid]

        if target == guess:
            return mid
        elif guess < target:
            start = mid + 1
        else:
            end = mid - 1

    return end


# print(floor(arr, 1))


def nextGreatestLetter(letters, target):

    start = 0
    end = len(letters) - 1

    while start <= end:
        mid = (start + end) // 2
        guess = letters[mid]

        if guess < target:
            start = mid + 1
        else:
            end = mid - 1
        print(mid)

    return letters[start % len(letters)]


# print(nextGreatestLetter(['c', 'f', 'j'], 'a'))


def search(nums, target, findStartIndex):

    ans = -1
    start = 0
    end = len(nums) - 1

    while start <= end:
        mid = (start + end) // 2

        if target == nums[mid]:
            ans = mid
            if findStartIndex:
                end = mid - 1
            else:
                start = mid + 1

        elif target > nums[mid]:
            start = mid + 1
        else:
            end = mid - 1

    return ans


def searchRange(nums, target):

    res = [-1, -1]

    res[0] = search(nums, target, True)
    if res[0] != -1:
        res[1] = search(nums, target, False)

    return res


# print(searchRange([5, 7, 7, 8, 8, 10], 8))


def findRange(arr, target):
    # first find the range
    # first start with a box of size 2
    start = 0
    end = 1

    # condition for the target to lie in the range
    while target > arr[end]:
        temp = end + 1
        # double the box value
        end = end + (end - start + 1) * 2
        start = temp

    return binarySearch(arr, target, start, end)


def binarySearch(arr, target, start, end):

    while start <= end:
        mid = (start + end) // 2
        mid_item = arr[mid]

        if mid_item == target:
            return mid
        if mid_item < target:
            start = mid + 1
        else:
            end = mid - 1

    return None


arr = [3, 5, 7, 9, 10, 90, 100, 130, 140, 160, 170]
target = 10

# print(findRange(arr, target))


def bitonic(arr):
    start = 0
    end = len(arr) - 1

    while start < end:
        mid = (start + end) // 2

        if arr[mid] > arr[mid + 1]:
            end = mid
        else:
            start = mid + 1

    return start


# print(bitonic([1, 2, 3, 5, 6, 7, 5, 4, 3, 2]))


def sqrt(x):
    start = 0
    end = x

    while start <= end:
        mid = (start + end) // 2

        if mid * mid > x:
            end = mid - 1
        elif mid * mid < x:
            start = mid + 1
        else:
            return mid

    return end


# print(sqrt(11))


def twoSum(arr, target):
    start = 0
    end = len(arr) - 1

    while start <= end:

        if arr[start] + arr[end] == target:
            return [start + 1, end + 1]
        if arr[start] + arr[end] > target:
            end -= 1
        else:
            start += 1


test1 = [2, 7, 11, 15]
target1 = 18

test2 = [2, 3, 4]
target2 = 6

test3 = [-1, 0]
target3 = -1

target4 = 542
# print(test4[23], test4[31])
# print(twoSum(test4, target4))


def arrangeCoins(n):
    start = 0
    end = n

    while start <= end:
        mid = (start + end) // 2
        k = (mid * (mid + 1)) // 2

        if k == n:
            return mid

        if k < n:
            start = mid + 1
        else:
            end = mid - 1

    return end


# print(arrangeCoins(8))


def singleNonDuplicate(nums):
    start = 0
    end = len(nums) - 1

    while start <= end:
        mid = (start + end) // 2
        mid = mid - 1 if mid % 2 == 1 else mid

        if mid - 1 >= 0 and nums[mid] == nums[mid - 1]:
            end = mid - 2
        elif mid + 1 <= len(nums) - 1 and nums[mid] == nums[mid + 1]:
            start = mid + 2
        else:
            return nums[mid]


nums = [1, 1, 2, 3, 3, 4, 4, 8, 8]

# print(singleNonDuplicate(nums))

action = ["TimeMap", "set", "set", "get", "get", "get", "get", "get"]
values = [
    [],
    ["love", "high", 10],
    ["love", "low", 20],
    ["love", 5],
    ["love", 10],
    ["love", 15],
    ["love", 20],
    ["love", 25],
]


class TimeMap:
    def __init__(self):
        self.hashTable = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashTable[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        start = 0
        end = len(self.hashTable[key]) - 1

        while start <= end:
            mid = (start + end) // 2

            if self.hashTable[key][mid][1] == timestamp:
                return self.hashTable[key][mid][0]

            if self.hashTable[key][mid][1] < timestamp:
                start = mid + 1
            else:
                end = mid - 1

        if end < 0:
            return ""

        return self.hashTable[key][end][0]


# timeMap = TimeMap()

# timeMap.set("love", "high", 10)
# timeMap.set("love", "low", 20)

# print("Should print empty", timeMap.get("love", 5))  # print ''
# print("Should print high", timeMap.get("love", 10))  # print 'high'
# print("Should print high", timeMap.get("love", 15))  # print 'high'
# print("Should print low", timeMap.get("love", 20))  # print 'low'
# print("Should print low", timeMap.get("love", 25))  # print 'low'


def shipWithinDays(weights, days):
    start = 0
    end = len(weights) - 1

    while start <= end:
        mid = (start + end) // 2
        maxCap = 0

        for i in range(0, mid + 1):
            maxCap += weights[i]

        totalPackages = 0
        track = mid + 1

        for i in range(mid + 1, len(weights)):
            sum = 0

            while sum <= maxCap and track < len(weights):
                sum += weights[track]
                track += 1

            totalPackages += 1

        print("totalPackages", totalPackages)
        print("d")

        if totalPackages == days:
            return maxCap

        if totalPackages > days:
            start = mid

        else:
            end = mid


weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
days = 5

weights2 = [3, 2, 2, 4, 1, 4]
days2 = 3

# print(shipWithinDays(weights2, days2))


def can_ship(candidate, weights, days):
    curr_weight = 0
    days_taken = 1

    for weight in weights:
        curr_weight += weight

        if curr_weight > candidate:
            days_taken += 1
            curr_weight = weight

    return days_taken <= days


def shipWithinDays2(weights, days):
    start = max(weights)
    end = sum(weights)

    while start < end:
        mid = (start + end) // 2

        if can_ship(mid, weights, days):
            end = mid
        else:
            start = mid + 1

    return end


weights3 = [1, 2, 3, 1, 1]
days3 = 4

# print(shipWithinDays2(weights3, days3))


class Solution:
    def findInMountainArray(self, target: int, mountain_arr) -> int:

        peak = bitonic(mountain_arr)
        firstSection = self.search(mountain_arr, target, 0, peak)

        if firstSection != -1:
            return firstSection
        else:
            return self.search(mountain_arr, target, peak, len(mountain_arr) - 1)

    def search(self, mountain_arr, target, start, end):
        start = 0
        end = len(mountain_arr) - 1

        while start <= end:
            mid = (start + end) // 2

            if mountain_arr[mid] == target:
                return mid

            if mountain_arr[mid] < target:
                start = mid + 1
            else:
                end = mid - 1

        return -1


solution = Solution()

print(
    solution.findInMountainArray(
        3,
        [0, 5, 3, 1],
    )
)
