
function isPrime(n) {
    if (n <= 1) return false

    //check from 2 to n -1
    for (var i = 2; i < n; i++) {
        if (n%i == 0) return false
    }

    return true
}


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


function primeFactors(n) {
    //print the number of 2s that divide n
    while (n % 2 == 0) {
        console.log(2)
        n = n / 2
    }

    //n must be odd at this point. so we can skip one element
    //(Note i = i + 2)
    for (var i = 3; i*i <= n; i = i + 2) {
        //while i divides n, print i and divide n
        while (n % i == 0) {
            console.log(i)
            n = n / i
        }
    }

    //when n is a prime number greater than 2
    if (n > 2) {
        console.log(n)
    }
}

primeFactors(120)
//console.log(isPrimeOpt(101))
