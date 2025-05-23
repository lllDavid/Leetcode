int longestSubarray(int* nums, int numsSize) {
    int maxVal = nums[0], maxLen = 0, curLen = 0;

    for (int i = 0; i < numsSize; i++) {
        if (nums[i] > maxVal) {
            maxVal = nums[i];
            curLen = 1;
        } else if (nums[i] == maxVal) {
            curLen++;
        } else {
            curLen = 0;
        }
        if (curLen > maxLen)
            maxLen = curLen;
    }

    return maxLen;
}