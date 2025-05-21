/**
 * // Definition for a _Node.
 * function _Node(val,prev,next,child) {
 *    this.val = val;
 *    this.prev = prev;
 *    this.next = next;
 *    this.child = child;
 * };
 */

/**
 * @param {_Node} head
 * @return {_Node}
 */
var flatten = function (head) {
    if (!head) return head;

    let stack = [];
    let curr = head;

    while (curr) {
        if (curr.child) {
            if (curr.next) {
                stack.push(curr.next);
            }

            curr.next = curr.child;
            curr.child.prev = curr;
            curr.child = null; 

        } else if (!curr.next && stack.length > 0) {
            let nextNode = stack.pop();
            curr.next = nextNode;
            nextNode.prev = curr;
        }

        curr = curr.next;
    }

    return head;
};