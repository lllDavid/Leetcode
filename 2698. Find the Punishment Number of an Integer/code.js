/**
 * @param {number} n
 * @return {number}
 */
var punishmentNumber = function (n) {
    let total = 0;

    function canPartition(s, target, index = 0, sum = 0) {
        if (index === s.length) return sum === target;

        for (let i = index + 1; i <= s.length; i++) {
            let num = parseInt(s.slice(index, i), 10);
            if (canPartition(s, target, i, sum + num)) return true;
        }
        return false;
    }

    for (let i = 1; i <= n; i++) {
        let squareStr = (i * i).toString();
        if (canPartition(squareStr, i)) {
            total += i * i;
        }
    }

    return total;
};