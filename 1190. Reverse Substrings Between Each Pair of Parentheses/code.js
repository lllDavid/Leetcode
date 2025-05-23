/**
 * @param {string} s
 * @return {string}
 */
var reverseParentheses = function (s) {
    let stack = [];
    for (let c of s) {
        if (c === ')') {
            let temp = '';
            while (stack[stack.length - 1] !== '(') temp += stack.pop();
            stack.pop();
            stack.push(...temp);
        } else stack.push(c);
    }
    return stack.join('');
};