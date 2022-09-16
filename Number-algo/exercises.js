
function isPrimeOpt(n) {
    if (n <= 1) return false
    if (n <= 3) return true

    //this is checked so we can skip middle five
    //elements in below loop
    if (n % 2 === 0 || n % 3 === 0) return false

    for (var i = 5; i*i <= n; i = i + 6) {
        console.log(i)
        if (n % i === 0 || n % (i + 2) === 0) {
            return false
        }
    }

    return true
}

function modularExponentiation(base, exponent, modulus) {
    if (modulus === 1) return 0

    var value = 1

    for (var i = 0; i < exponent; i++) {
        value = (value * base) % modulus
    }

    return value
}


function allPrimeslessThanN(n) {
    for (var i = 0; i < n; i++) {
        if (isPrimeOpt(i)) {
            console.log(i)
        }
    }
}


function maxDivide(number, divisor) {
    while (number % divisor == 0) {
        number /= divisor
    }

    return number
}


function isUgly(number) {
    number = maxDivide(number, 2)
    number = maxDivide(number, 3)
    number = maxDivide(number, 5)

    return number == 1
}


function arrayNUglyNumbers(n) {
    var counter = 0, currentNumber = 1, uglyNumbers = []

    while (counter != n) {
        if (isUgly(currentNumber)) {
            //counter++
            uglyNumbers.push(currentNumber)
        }
        counter++
        currentNumber++
    }

    return uglyNumbers
}

// 

function isUglyOpt(n) {
    var uglyNums = [2, 3, 5] 

    if (n === 1) return true

    for (var i = 2; i <= 5; i++) {
        if (!uglyNums.includes(i)) {
            continue
        }else {
            while (n % i === 0) {
                n /= i
            }
        }
    }

    return n === 1
}

console.log(isUglyOpt(16))