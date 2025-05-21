/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* createTargetArray(int* nums, int numsSize, int* index, int indexSize, int* returnSize) {
    int* target = (int*)malloc(sizeof(int) * numsSize);
    int i, j;
    
    *returnSize = numsSize;

    for (i = 0; i < numsSize; i++) {
        for (j = i; j > index[i]; j--) {
            target[j] = target[j - 1];
        }
        target[index[i]] = nums[i];
    }

    return target;
}
