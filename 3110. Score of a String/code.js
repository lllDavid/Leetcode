/**
 * @param {string} s
 * @return {number}
 */
var scoreOfString = function (s) {
    let sum = 0
    let n = s.length
    for (let i = 0; i < n - 1; i++) {
        let diff = Math.abs(s.charCodeAt(i) - s.charCodeAt(i + 1));
        sum += diff
    }
    return sum
};