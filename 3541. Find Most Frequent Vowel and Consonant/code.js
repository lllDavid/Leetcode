/**
 * @param {string} s
 * @return {number}
 */
var maxFreqSum = function (s) {
    const vowels = new Set(['a', 'e', 'i', 'o', 'u']);
    const freq = {};

    for (const char of s) {
        freq[char] = (freq[char] || 0) + 1;
    }

    let maxVowelFreq = 0;
    let maxConsonantFreq = 0;

    for (const [char, count] of Object.entries(freq)) {
        if (vowels.has(char)) {
            if (count > maxVowelFreq) maxVowelFreq = count;
        } else {
            if (count > maxConsonantFreq) maxConsonantFreq = count;
        }
    }

    return maxVowelFreq + maxConsonantFreq;
};