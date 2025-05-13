/**
 * @param {string} s
 * @return {number}
 */
var maxDepth = function(s) {
    let max = 0;
    let currentDepth = 0;

    for (let char of s) {
        if (char === '(') {
            currentDepth++;
            max = Math.max(max, currentDepth);
        } else if (char === ')') {
            currentDepth--;
        }
    }

    return max;
};
