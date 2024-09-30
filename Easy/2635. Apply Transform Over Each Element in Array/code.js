/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function (arr, fn) {
    let arr2 = []

    for (let i in arr) {
        arr2.push(fn(arr[i], parseInt(i)))
    }
    return arr2
};