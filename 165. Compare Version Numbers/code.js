/**
 * @param {string} version1
 * @param {string} version2
 * @return {number}
 */
var compareVersion = function(version1, version2) {
    const arrayV1 = version1.split(".").map(Number);
    const arrayV2 = version2.split(".").map(Number);

    let i = 0;

    while (i < arrayV1.length || i < arrayV2.length) {
        const v1 = arrayV1[i] || 0; 
        const v2 = arrayV2[i] || 0; 

        if (v1 > v2) {
            return 1;
        } else if (v2 > v1) {
            return -1;
        }
        
        i++;
    }
    return 0;
};
