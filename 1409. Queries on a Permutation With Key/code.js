/**
 * @param {number[]} queries
 * @param {number} m
 * @return {number[]}
 */
var processQueries = function(queries, m) {
    let P = Array.from({length: m}, (_, i) => i + 1); 
    let result = [];

    for (let q of queries) {
        let index = P.indexOf(q);
        result.push(index);
        
        P.splice(index, 1);
        
        P.unshift(q);
    }

    return result;
};
