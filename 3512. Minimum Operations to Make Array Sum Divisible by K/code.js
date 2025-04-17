/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var minOperations = function (nums, k) {
    let sum = nums.reduce((acc, num) => acc + num, 0);
    return sum % k;
};