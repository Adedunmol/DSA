

function selectionSort(arr) {
    
    for (let i = 0; i < arr.length - 1; i++) {
        
        let smallest = i
        for (let j = i + 1; j < arr.length; j++) {
            if (arr[j] < arr[smallest]) {
                smallest = j
            }
        }
        
        [arr[i], arr[smallest]] = [arr[smallest], arr[i]]
    }

    return arr
}

const arr = [5, 3, 6, 2, 10]


console.log(selectionSort(arr))