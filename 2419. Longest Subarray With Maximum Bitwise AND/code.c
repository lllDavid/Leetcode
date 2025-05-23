int longestSubarray(int* nums, int numsSize) {
    int maxVal = nums[0];
    for (int i = 1; i < numsSize; i++) {
        if (nums[i] > maxVal)
            maxVal = nums[i];
    }

    int maxLen = 0, curLen = 0;
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] == maxVal) {
            curLen++;
            if (curLen > maxLen)
                maxLen = curLen;
        } else {
            curLen = 0;
        }
    }
    return maxLen;
}