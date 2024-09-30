/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function (arr, fn) {
    filteredArr = []

    for (i in arr) {
        if (fn(arr[i], Number(i))) {
            filteredArr.push(arr[i])
        }
    }
    return filteredArr
};