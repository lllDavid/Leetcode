/**
 * @param {string} s
 * @param {string} t
 * @return {character}
 */
var findTheDifference = function (s, t) {
    const chars = {}
    if (s === "") {
        return t
    }
    for (let char of s) {
        chars[char] = (chars[char] || 0) + 1
    }

    for (let char of t) {
        if (!chars[char]) {
            return char
        }
        chars[char]--
    }

};