int findPermutationDifference(char* s, char* t) {
    int sIndex[128] = {0}; 

    for (int i = 0; s[i]; i++) {
        sIndex[(int)s[i]] = i;
    }

    int diff = 0;
    
    for (int i = 0; t[i]; i++) {
        diff += abs(i - sIndex[(int)t[i]]);
    }

    return diff;
}