/**
 * @param {number[]} arr
 * @param {number} k
 * @return {number}
 */
var findLeastNumOfUniqueInts = function (arr, k) {
    const freq = {};
    for (const num of arr) freq[num] = (freq[num] || 0) + 1;

    const counts = Object.values(freq).sort((a, b) => a - b);

    let unique = counts.length;
    for (const c of counts) {
        if (k >= c) {
            k -= c;
            unique--;
        } else break;
    }
    return unique;
};