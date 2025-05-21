/**
 * @param {number[]} nums
 * @return {number}
 */
var countDistinctIntegers = function (nums) {
    const seen = new Set();

    for (let num of nums) {
        seen.add(num);
        const reversed = parseInt(num.toString().split('').reverse().join(''), 10);
        seen.add(reversed);
    }

    return seen.size;
};