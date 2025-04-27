/**
 * @param {number} num
 * @return {number}
 */
var minimumSum = function (num) {
    let digits = String(num).split('').map(Number);
    digits.sort((a, b) => a - b);

    let new1 = digits[0] * 10 + digits[2];
    let new2 = digits[1] * 10 + digits[3];

    return new1 + new2;
};