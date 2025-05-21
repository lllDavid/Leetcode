/**
 * @param {number[]} piles
 * @return {number}
 */
var maxCoins = function(piles) {
    piles.sort((a, b) => b - a); 
    let coins = 0;
    let n = piles.length / 3;
    
    for (let i = 1; i < 2 * n; i += 2) {
        coins += piles[i]; 
    }
    
    return coins;
};
