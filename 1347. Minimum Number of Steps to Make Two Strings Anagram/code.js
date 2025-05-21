/**
 * @param {string} s
 * @param {string} t
 * @return {number}
 */
var minSteps = function (s, t) {
    const count = new Array(26).fill(0);
    const aCharCode = 'a'.charCodeAt(0);

    for (let char of s) {
        count[char.charCodeAt(0) - aCharCode]++;
    }

    for (let char of t) {
        count[char.charCodeAt(0) - aCharCode]--;
    }

    let steps = 0;
    for (let num of count) {
        if (num > 0) steps += num;
    }

    return steps;
};