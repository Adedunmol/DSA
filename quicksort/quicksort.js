


function quickSort(arr, low=0, high=arr.length - 1) {
    if (low < high) {
        pIdx = partition(arr, low, high)
        quickSort(arr, low, pIdx - 1)
        quickSort(arr, pIdx + 1, high)
    }

    return arr
}


function partition(arr, low, high){
    let i = low - 1
    pivot = high

    for (let j = low; j <= high - 1; j++) {
        if (arr[j] <= arr[pivot]) {
            i++
            [arr[i], arr[j]] = [arr[j], arr[i]]
        }
    }
    i++
    [arr[pivot], arr[i]] = [arr[i], arr[pivot]]

    return i
}

let newArr = [10, 16, 8, 12, 15, 6, 3, 9, 5]
let arr = [33, 15, 10]

console.log(quickSort(newArr, 0, newArr.length - 1))