/**
 * @param {number} n
 * @param {number} k
 * @return {string}
 */
var getHappyString = function (n, k) {
    const result = [];

    function backtrack(path) {
        if (path.length === n) {
            result.push(path);
            return;
        }

        for (const ch of ['a', 'b', 'c']) {
            if (path.length === 0 || path[path.length - 1] !== ch) {
                backtrack(path + ch);
            }
        }
    }

    backtrack("");

    return result.length >= k ? result[k - 1] : "";
};