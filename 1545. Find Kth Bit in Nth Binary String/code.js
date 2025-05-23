/**
 * @param {number} n
 * @param {number} k
 * @return {character}
 */
var findKthBit = function (n, k) {
    if (n === 1) return '0';

    const mid = (1 << (n - 1));

    if (k === mid) return '1';
    if (k < mid) return findKthBit(n - 1, k);

    const mirrorPos = 2 * mid - k;
    return findKthBit(n - 1, mirrorPos) === '0' ? '1' : '0';
};