/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var longestSubsequence = function (s, k) {
    let zeroCount = 0;
    for (const c of s) {
        if (c === '0') zeroCount++;
    }

    let oneCount = 0;
    let value = 0;
    let weight = 1;

    for (let i = s.length - 1; i >= 0 && value + weight <= k; i--) {
        if (s[i] === '1') {
            oneCount++;
            value += weight;
        }
        weight <<= 1;
    }

    return zeroCount + oneCount;

};