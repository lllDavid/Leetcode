/**
 * @param {number} start
 * @param {number} goal
 * @return {number}
 */
var minBitFlips = function (start, goal) {
    let xor = start ^ goal;
    let count = 0;

    while (xor > 0) {
        count += xor & 1; 
        xor = xor >> 1;   
    }

    return count;
};