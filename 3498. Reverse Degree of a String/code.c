int reverseDegree(char* s) {
    int degree = 0;
    int length = strlen(s);
    
    for (int i = 0; i < length; i++) {
        char ch = s[i];
        int reverse_position = 26 - (ch - 'a');
        degree += reverse_position * (i + 1);  
    }
    
    return degree;
}