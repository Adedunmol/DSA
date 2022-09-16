


import collections
import math
from operator import truediv
import sys
from unittest import result


def check_palindrome(word):
    low = 0
    high = len(word) - 1

    while low <= high:
        
        if word[low] == word[high]:
            low += 1
            high -= 1
        else:
            return False
    
    return True


#print(check_palindrome('deified'))


def check_palindrome_with_special_chars(word):
    letters = 'abcdefghijklmnopqrstuvxyz'
    numbers = '0123456789'
    low = 0
    high = len(word) - 1

    while low <= high:

        if word[low].lower() in letters or word[low].lower() in numbers:
            if word[high].lower() in letters or word[high].lower() in numbers:
                if word[low].lower() == word[high].lower():
                    low += 1
                    high -= 1
                else:
                    return False
            else:
                high -= 1
        else:
            low += 1
    
    return True


#print(check_palindrome_with_special_chars("Do geese see God"))

def max_in_sub_array(arr, k):
    maxValue = 0
    currentWindowValue = 0

    for i in range(len(arr)):
        currentWindowValue += arr[i]

        if i >= k - 1:
            maxValue = max(maxValue, currentWindowValue)
            currentWindowValue -= arr[i - (k - 1)]
    
    return maxValue


#print(max_in_sub_array([5, 1, 9, 7, 6, 4], 3))



def substring_without_repeating_chars(word):
    words = {}
    currentWindowSize = 0
    windowStart = 0
    maxValue = 0

    for windowEnd in range(len(word)):
        if not words.get(word[windowEnd]):
            words[word[windowEnd]] = windowEnd
            currentWindowSize += 1
        else:
            maxValue = max(maxValue, currentWindowSize)
            currentWindowSize -= words.get(word[windowEnd]) - windowStart + 1
            windowStart = words.get(word[windowEnd]) + 1
            words[word[windowEnd]] = windowEnd
            
        print(maxValue)

    return maxValue

#print(substring_without_repeating_chars('abcabcbb'))


def minSubArray(arr, target):
    minWindowLength = sys.maxsize
    currentWindowSum = 0
    windowStart = 0

    for windowEnd in range(len(arr)):
        currentWindowSum += arr[windowEnd]

        while currentWindowSum >= target:
            minWindowLength = min(minWindowLength, windowEnd - windowStart + 1)
            currentWindowSum -= arr[windowStart]
            windowStart += 1
    
    return minWindowLength


#print(minSubArray([4, 2, 2, 7, 8, 1, 2, 8, 1, 0], 9))


def reversePrefix(word: str, ch: str) -> str:
    newWord = list(word)
    start = 0
    end = 0
    while end < len(word):
        if word[end] == ch:
            while start < end:
                print(end)
                newWord[start], newWord[end] = newWord[end], newWord[start]
                start += 1
                end -= 1
            return ''.join(newWord)
                
        end += 1
    return word

    
def numIdenticalPairs(nums):

    count = {}
    res = 0

    for i in range(len(nums)):

        if count.get(nums[i]):
            count[nums[i]] += 1
        else:
            count[nums[i]] = 1


    for key, value in count.items():

        if value > 1:
            res += (value * (value - 1)) // 2
    

    return res

arr = [2, 5, 1, 3, 4, 7]

#print(numIdenticalPairs([1,1,1,1]))


def commonElements(kArray):
    hashTable = {}
    last = None
    result = []

    for array in kArray:
        last = None
        for element in array:
            if last != element:
                if not hashTable.get(element):
                    hashTable[element] = 1
                else:
                    hashTable[element] += 1
            last = element
    

    for key, value in hashTable.items():
        if (value == len(kArray)):
            result.append(key)
    

    return result


#print(commonElements([[1, 2, 3], [1, 2, 3, 4], [1, 2]]))

def pangram(sentence):
    hashTable = {}
    result = 0

    if len(sentence) < 26:
        return False

    for letter in sentence:
        if not hashTable.get(letter):
            hashTable[letter] = True
            result += 1

    return result == 26


# print(pangram("leetcode"))

def highestAltitude(gain):

    res = 0
    sumOfAltitudes = 0

    if len(gain) < 2:
        return max(res, gain[0])

    for i in gain:
        sumOfAltitudes += i
        res = max(res, sumOfAltitudes)

    return res


# print(highestAltitude([-4,-3,-2,-1,4,3,2]))

def flipAndInvertImage(images):

    for i in range(len(images)):
        arr = images[i]
        arr.reverse()   
        for j in range(len(arr)):
            if arr[j] == 1:
                arr[j] = 0
            elif arr[j] == 0:
                arr[j] = 1
    
        images[i] = arr

    return images


#print(flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]))

def diagonalSum(matrix):
    total = 0
    midValue = None

    if len(matrix) < 2:
        return matrix[0][0]

    if len(matrix) % 2 != 0:
        grid = len(matrix) // 2
        midValue = matrix[grid][grid]

    for i in range(len(matrix)):
        total += matrix[i][i]
        
        if i != len(matrix) // 2 or matrix[i][len(matrix[i]) - i - 1] != midValue:
            total += matrix[i][len(matrix[i]) - i - 1]
            print(matrix[i][len(matrix[i]) - i - 1])


    return total

#print(diagonalSum([
            #[15,16,3,17,7,6,2],
            #[2,14,18,17,18,15,19],
            #[9,3,2,4,5,20,12],
            #[2,9,7,15,2,2,8],
            #[19,9,12,16,20,14,19],
            #[13,16,18,5,5,13,18],
            #[1,19,5,4,2,1,18]]))


def isAnagram(s, t):
    sLetters = {}
    tLetters = {}

    if len(s) != len(t):
        return False

    for i in range(len(s)):
        if not sLetters.get(s[i]):
            sLetters[s[i]] = 1
        else:
            sLetters[s[i]] += 1
        
        if not tLetters.get(t[i]):
            tLetters[t[i]] = 1
        else:
            tLetters[t[i]] += 1
    
    for key, value in sLetters.items():
        if not tLetters.get(key):
            return False

        if sLetters[key] != tLetters[key]:
            return False

    return True

def isAnagramOpt(s, t):
    s = ''.join(sorted(s))
    t = ''.join(sorted(t))

    if len(s) != len(t):
        return False

    for i in range(len(s)):
        if s[i] != t[i]:
            return False

    return True


def isAnagramOpt2(s, t):

    if len(s) != len(t):
        return False

    return

#print(isAnagramOpt('rat', 'car'))

def twoSum(nums, target):

    hashTable = {}
        
    for i in range(len(nums)):
        difference = target - nums[i]

        if hashTable.get(difference) is not None:
            return [i, hashTable[difference]]
        else:
            hashTable[nums[i]] = i
            print(hashTable)
        
    return []

#print(twoSum([2,7,11,15], 9))

def groupAnagrams(arr):

    if len(arr) < 2:
        return [[arr[0]]]

    words = {}
    result = []

    for i in arr:
        if ''.join(sorted(i)) in words:
            words[''.join(sorted(i))].append(i)
        else:
            words[''.join(sorted(i))] = [i]
    
    for key, value in words.items():
        result.append(value)

    return result

#print(groupAnagrams(arr))


def removeDuplicates(nums):
        
    i = 0 
    total = 1
        
    for j in range(1, len(nums)):
            
        if nums[i] == nums[j]:
            nums[j] = '_'
        else:
            i+=1 
            total += 1
            nums[j], nums[i] = nums[i], nums[j]
                
    return total, nums


#print(removeDuplicates([1, 1, 2]))


def countLucky(grid):
    result = []
    maxInCol = []
    minInRow = [] 

    for row in grid:
        minElement = row[0]
        for i in row:
            minElement = min(minElement, i)
        minInRow.append(minElement)


    for col in range(len(grid[0])):
        maxElement = 0
        for row in range(len(grid)):
            maxElement = max(maxElement, grid[row][col])
        maxInCol.append(maxElement)

    for i in maxInCol:
        if i in minInRow:
            result.append(i)

    return result


def spiralOrder(matrix):

    result = []
    
    if len(matrix) < 2:
        result.extend(matrix[0])
        return result

    topRow = 0
    rightCol = len(matrix[0]) - 1
    btmRow = len(matrix) - 1
    leftCol = 0
        
    while topRow <= btmRow and leftCol <= rightCol:

        for i in range(leftCol, rightCol + 1):
            result.append(matrix[topRow][i])
            
        topRow += 1
        print('top row', result)
        for i in range(topRow, btmRow + 1):
            result.append(matrix[i][rightCol])
    
        rightCol -= 1
        print('right col', result)

        if topRow <= btmRow:
            for i in range(rightCol, leftCol - 1, -1):
                result.append(matrix[btmRow][i])
            
            btmRow -= 1
            print('bottom row', result)


        if leftCol <= rightCol:
            for i in range(btmRow, topRow - 1, -1):
                result.append(matrix[i][leftCol])
            
            leftCol += 1
            print('left column', result)

            
        
    return result


#mat = [1,11],
    [2,12],
    [3,13],
    [4,14],
    [5,15],
    [6,16],
    [7,17],
    [8,18],
    [9,19],
    [10,20]

#print(spiralOrder([]))


def validPalindrome(s):

    def isPal(l, r):
        print(s[l:r])
        print(s[r:l:-1])
        print(s[l:r] == s[r:l:-1] )
        return s[l:r] == s[r:l:-1]                      
            
    l, r = 0, len(s) - 1
    skip = 0
    while l < r:
        if s[l] == s[r]:
            l += 1
            r -= 1
        else:
            return isPal(l, r - 1) or isPal(l + 1, r)
    return True


#print(validPalindrome("eeccccbebaeeabebccceea"))

def topKFrequent(nums, k):
    
    hashTable = {}
    freq = [[] for i in range(len(nums) + 1)]

    for i in nums:
        hashTable[i] = 1 + hashTable.get(i, 0)

    for key, value in hashTable.items():
        freq[value].append(key)
    
    result = []

    for i in range(len(freq) - 1, 0, -1):

        for j in freq[i]:
            result.append(j)

            if len(result) == k:
                return result


# print(topKFrequent([5, 3, 1, 1, 1, 3, 73, 1], 3))

def isValidSudoku(board):
    hashTable = {}
    grid = {0, 3, 6}

    for i in range(len(board)):
        axis = f'{i} row'
        hashTable[axis] = set()

        for j in range(len(board)):
            if board[i][j] != '.':
                if board[i][j] in hashTable[axis]:
                    return False
                else:
                    hashTable[axis].add(board[i][j])

        
        axis = f'{i} col'
        hashTable[axis] = set()

        for j in range(len(board)):

            if board[j][i] != '.':
                if board[j][i] in hashTable[axis]:
                    return False
                else:
                    hashTable[axis].add(board[j][i])


    return True

board = [
["5","3",".",".","7",".",".",".","."],
["6",".",".","1","9","5",".",".","."],
[".","9","8",".",".",".",".","6","."],
["8",".",".",".","6",".",".",".","3"],
["4",".",".","8",".","3",".",".","1"],
["7",".",".",".","2",".",".",".","6"],
[".","6",".",".",".",".","2","8","."],
[".",".",".","4","1","9",".",".","5"],
[".",".",".",".","8",".",".","7","9"]]


# print(isValidSudoku(board))

def isValidSudoku2(board):
    cols = collections.defaultdict(set)
    rows = collections.defaultdict(set)
    squares = collections.defaultdict(set)

    for r in range(9):
        for c in range(9):
            if board[r][c] == '.':
                continue
            if (board[r][c] in rows[r] or 
                board[r][c] in cols[c] or
                board[r][c] in squares[(r // 3, c // 3)]):
                return False
                
            cols[c].add(board[r][c])
            rows[r].add(board[r][c])
            squares[(r // 3, c // 3)].add(board[r][c])

    return True

print(isValidSudoku2(board))