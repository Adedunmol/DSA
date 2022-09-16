const { hash } = require("bcrypt")


function check_palindrome(word) {
    const letters = 'abcdefghijklmnopqrstuvxyz'
    const numbers = '0123456789'
    let low = 0
    let high = word.length - 1

    while (low <= high) {
        if (letters.includes(word[low].toLowerCase()) || numbers.includes(word[low])) {
            if (letters.includes(word[high].toLowerCase()) || numbers.includes(word[high])) {
                if (word[low].toLowerCase() === word[high].toLowerCase()) {
                    low++
                    high--
                }else {
                    return false
                }
            }else {
                high--
            }
        }else {
            low++
        }
    }

    return true
}

// console.log(check_palindrome('Taco cat'))


function toLower(str) {
    var asciiForUpperCaseA = 65 
    var asciiForUpperCaseB = 90
    
    var result = []

    for (var i = 0; i < str.length - 1; i++) {
        if (65 <= str.charCodeAt(i) <= 90) {

            if (str.charCodeAt(i) <= 90) {
                var letter = str.charCodeAt(i) + 32
                letter = String.fromCharCode(letter)
                result.push(letter)
            }
        }else {
            result.push(str.charAt(i))
        }
    }

    return result.join('')
}


// var uri = 'http://your.domain/product.aspx?category=4&product_id=2140&query=lcd+tv'
// var queryString = {}

// uri.replace(new RegExp("([^?=&]+)(=[^&])*", 'g'))

var reversePrefix = function(word, ch) {
    var newWord = word.split('')
    var start = 0
    var end = 0
    while (end < word.length) {
        if (word.charAt(end) == ch) {
            while (start < end) {
                [newWord[start], newWord[end]] = [newWord[end], newWord[start]]
                start += 1
                end -= 1
            }
            return newWord.join('')

        }   
        end += 1
    }

    return word
};

// console.log(reversePrefix('abcdefd', 'd'))

function findSum(arr, weight) {
    var hashTable = {}

    for (var i = 0; i < arr.length; i++) {
        var currentElement = arr[i], difference = weight - currentElement

        if (hashTable[difference] != undefined) {
            return [i, hashTable[difference]]
        }else {
            hashTable[currentElement] = i
        }
    }
    return -1
}

var arr = [1, 2, 3, 4, 5]
var weight = 7

//console.log(findSum(arr, weight))

function commonElements(kArray) {
    var hashMap = {}, last, answer = []

    for (var i = 0; i <kArray.length; i++) {
        var currentArray = kArray[i], last = null

        for (var j = 0; j < currentArray.length; j++) {
            var currentElement = currentArray[j]

            if (last != currentElement) {
                if (!hashMap[currentElement]) {
                    hashMap[currentElement] = 1
                }else {
                    hashMap[currentElement] += 1
                }
            }
            last = currentElement
        }
    }

    for (var prop in hashMap) {
        console.log(prop)
        if (hashMap[prop] === kArray.length) {
            answer.push(prop)
        }
    }

    return answer
}


//console.log(commonElements([[1, 2, 3], [1, 2, 3, 4], [1, 2]]))

function Matrix(rows, columns) {
    var jaggedArray = new Array(rows)
    for (var i = 0; i < columns; i++) {
        jaggedArray[i] = new Array(rows)
    }

    return jaggedArray
}

//console.log(Matrix(3, 3))

var matrix3by3 = [
                [1, 2, 3, 4, 5], 
                [6, 7, 8, 9, 10], 
                [11, 12, 13, 14, 15],
                [16, 17, 18, 19, 20]]


function spiralPrint(M) {
    var topRow = 0,
        leftCol = 0,
        rightCol = M[0].length - 1,
        btmRow = M.length - 1

        while (topRow < btmRow && leftCol < rightCol) {
            for (var col = 0; col <= rightCol; col++) {
                console.log(M[topRow][col])
            }
            topRow++
            for (var row = topRow; row <= btmRow; row++) {
                console.log(M[row][rightCol])
            }
            rightCol--
            if (topRow <= btmRow) {
                for (var col = rightCol; col >= 0; col--) {
                    console.log(M[btmRow][col])
                }
                btmRow--
            }
            if (leftCol <= rightCol) {
                for (var row = btmRow; row > topRow; row--) {
                    console.log(M[row][leftCol])
                }
                leftCol++
            }
        }
}

//spiralPrint(matrix3by3)

function checkRow(rowArr, letter) {
    for (var i = 0; i < 3; i++) {
        if (rowArr[i] != letter) {
            return false
        }
    }

    return true
}


function checkColumn(gameBoardMatrix, columnIndex, letter) {
    for (var i = 0; i < 3; i++) {
        if (gameBoardMatrix[i][columnIndex] != letter) {
            return false
        }
    }
    return true
}


function ticTacToeWinner(gameBoardMatrix, letter) {
    // Check rows
    var rowWin = checkRow(gameBoardMatrix[0], letter) ||
                checkRow(gameBoardMatrix[1], letter) ||
                checkRow(gameBoardMatrix[2], letter)

    var colWin = checkColumn(gameBoardMatrix, 0, letter) ||
                checkColumn(gameBoardMatrix, 1, letter) ||
                checkColumn(gameBoardMatrix, 2, letter)
    
    var diagonalWinLeftToRight = (gameBoardMatrix[0][0] == letter &&
                                gameBoardMatrix[1][1] == letter &&
                                gameBoardMatrix[2][2] == letter)


    var diagonalWinRightToLeft = (gameBoardMatrix[0][2] == letter &&
                                gameBoardMatrix[1][1] == letter &&
                                gameBoardMatrix[2][0] == letter)


    return rowWin || colWin || diagonalWinLeftToRight || diagonalWinRightToLeft
}

var board = [['O', '-', 'X'], ['-', 'O', '-'], ['-', 'X', 'O']]

//console.log(ticTacToeWinner(board, 'X'))
//console.log(ticTacToeWinner(board, 'O'))


var board = 
`%e%%%%%%%%%\n
%...%.%...%\n
%.%.%.%.%%%\n
%.%.......%\n
%.%%%%.%%.%\n
%.%.....%.%\n
%%%%%%%%%x%\n`

var rows = board.split('\n')

function generateColumnArr(arr) {
    return arr.split('')
}

var mazeMatrix = rows.map(generateColumnArr)


function findChar(char, mazeMatrix) {
    var row = mazeMatrix.length,
        column = mazeMatrix[0].length

        for (var i = 0; i < row; i++) {
            for (var j = 0; j < column; j++) {
                if (mazeMatrix[i][j] == char) {
                    return [i, j]
                }
            }
        }
}


function printMatrix(matrix) {
    var mazePrintStr = "",
        row = matrix.length,
        column = matrix[0].length

    for (var i = 0; i < row; i++) {
        for (var j = 0; j < column; j++) {
            mazePrintStr += mazeMatrix[i][j]
        }
        mazePrintStr += "\n"
    }
    console.log(mazePrintStr)
}

function mazePathFinder(mazeMatrix) {
    var row = mazeMatrix.length,
        column = mazeMatrix[0].length,
        startPos = findChar('e', mazeMatrix),
        endPos = findChar('x', mazeMatrix)

    path(startPos[0], startPos[1])

    function path(x, y) {
        if (x > y - 1 || y > column - 1 || x < 0 || y < 0) {
            return false
        }
    
    //Found
    if (x == endPos[0] && y == endPos[1]) {
        return true
    }

    if (mazeMatrix[x][y] == '%' || mazeMatrix[x][y] == '+') {
        return false
    }

    //Mark the current spot
    mazeMatrix[x][y] = '+'
    printMatrix(mazeMatrix)

    if (path(x, y - 1) || path(x + 1, y) || path(x, y + 1) || path(x - 1, y)) {
        return true
    }

    mazeMatrix[x][y] = '.'
    return false
}
}

//mazePathFinder(mazeMatrix)

function base10ToString(n) {
    var binaryString = ""

    function base10ToStringHelper(n) {
        if (n < 2) {
            binaryString += n
            return 
        }else {
            console.log('division')
            base10ToStringHelper(Math.floor(n / 2))
            console.log('modulus')
            base10ToStringHelper(n % 2)
        }
    }
    base10ToStringHelper(n)

    return binaryString
}


//console.log(base10ToString(10))
//console.log(Math.floor(5 / 2))

function swap(strArr, index1, index2) {
    var temp = strArr[index1]
        strArr[index1] = strArr[index2]
        strArr[index2] = temp
}


function permute(strArr, begin, end) {
    if (begin == end) {
        console.log(strArr)
    }else {
        for (var i = begin; i < end + 1; i++) {
            swap(strArr, begin, i)
            permute(strArr, begin + 1, end)
            swap(strArr, begin, i)
        }
    }
}

function permuteArray(strArr) {
    permute(strArr, 0, strArr.length - 1)
}


//permuteArray(['A', 'C', 'D'])


function flattenDictionary(dictionary) {
    var flattenedDictionary = {}

    function flattenDictionaryHelper(dictionary, propName) {
        console.log(dictionary)
        if (typeof dictionary != 'object') {
            
            flattenedDictionary[propName] = dictionary
            return
        }

        for (var prop in dictionary) {
            console.log(prop)
            console.log(propName)
            if (propName == '') {
                flattenDictionaryHelper(dictionary[prop], propName + prop)
            }else {
                flattenDictionaryHelper(dictionary[prop], propName + '.' + prop)
            }
        }
    }

    flattenDictionaryHelper(dictionary, '')
    return flattenedDictionary
}

var dictionary = {
    'key1': '1',
    'key2': {
        'a': '2',
        'b': '3',
        'c': {
            'd': '3',
            'e': '1'
        }
    }
}

console.log(flattenDictionary(dictionary))