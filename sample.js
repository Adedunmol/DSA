
function majorityElement(arr) {
    maxItem = Math.max(arr)
    console.log(maxItem)
    countArr = [0] * (maxItem + 1)

    for (let item of arr) {
        countArr[item]++
    }

    return countArr
}

console.log(majorityElement([3,2,3]))