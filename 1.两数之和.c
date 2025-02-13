/*
 * @lc app=leetcode.cn id=1 lang=c
 *
 * [1] 两数之和
 */

// @lc code=start
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

// 定义哈希表节点
typedef struct HashNode {
    int key; // 存放数组元素
    int value; // 存放数组下标
    struct HashNode* next;
} HashNode;

// 哈希函数
int hashFunction(int key, int size)
{
    return abs(key) % size; // abs()函数取绝对值
}

// 创建哈希表
HashNode** createHashTable(int size)
{
    HashNode** hashTable = (HashNode**)malloc(size * sizeof(HashNode*));

    // 初始化哈希表
    for (int i = 0; i < size; ++i) {
        hashTable[i] = NULL;
    }

    return hashTable;
}

// 插入哈希表
void insertHashTable(HashNode** hashTable, int key, int value, int size)
{
    int hashIndex = hashFunction(key, size);
    HashNode* newNode = (HashNode*)malloc(sizeof(HashNode));
    newNode->key = key;
    newNode->value = value;
    newNode->next = hashTable[hashIndex];
    hashTable[hashIndex] = newNode;
}

// 查找哈希表
HashNode* searchHashTable(HashNode** hashTable, int key, int size)
{
    int hashIndex = hashFunction(key, size);
    HashNode* node = hashTable[hashIndex];
    while (node != NULL) {
        if (node->key == key) {
            return node;
        }
        node = node->next;
    }
    return NULL;
}

// 释放哈希表
void freeHashTable(HashNode** hashTable, int size)
{
    for (int i = 0; i < size; ++i) {
        HashNode* current = hashTable[i];
        while (current != NULL) {
            HashNode* temp = current;
            current = current->next;
            free(temp);
        }
    }
    free(hashTable);
}

int* twoSum(int* nums, int numsSize, int target, int* returnSize)
{
    int hashTableSize = numsSize;
    HashNode** hashTable = createHashTable(hashTableSize);

    for (int i = 0; i < numsSize; ++i) {
        int complement = target - nums[i];
        HashNode* node = searchHashTable(hashTable, complement, hashTableSize);
        if (node != NULL) {
            int* results = (int*)malloc(2 * sizeof(int));
            results[0] = node->value;
            results[1] = i;
            *returnSize = 2;
            freeHashTable(hashTable, hashTableSize);
            return results;
        }
        insertHashTable(hashTable, nums[i], i, hashTableSize);
    }

    *returnSize = 0;
    freeHashTable(hashTable, hashTableSize);
    return NULL;
}

// @lc code=end
