

const binary_search = (list, target) => {
    low = 0
    high = list.length - 1

    while (low <= high) {
        mid = Math.floor((low + high) / 2)
        guess = list[mid]

        if (guess === target) {
            return mid
        }

        if (guess < target) {
            low = mid + 1
        }else {
            high = mid - 1
        }
    }

    return null
}

const my_list = [1, 3, 5, 7, 9]

//console.log(binary_search(my_list, 10))



const binary_search_rotated = (list, target) => {
    low = 0
    high = list.length - 1

    while (low <= high) {
        mid = Math.floor((low + high) / 2)
        guess = list[mid]

        if (guess === target) {
            return mid
        }

        if (guess < list[high]) {

            if (target < list[high]) {
                
                if (guess < target) {
                    low = mid + 1
                }else {
                    high = mid - 1
                }
            }else if (target === list[high]) {
                low = mid + 1
            }else {
                high = mid - 1
            }
        }else {
            if (target > list[high]) {
                if (guess > target) {
                    high = mid - 1
                }else {
                    low = mid + 1
                }
            }else {
                low = mid + 1
            }
        }
    }

    return null
}


const my_list2 = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]

const result = binary_search_rotated(my_list2, 10)
