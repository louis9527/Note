import time


def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for i in range(len(nums)):
        j = target - nums[i]
        if (j in nums) and (nums.index(j) != i):
            return [i, nums.index(j)]


def sum_index(nums, target=100):
    start = 0
    end = len(nums) - 1
    while not start == len(nums) - 1:
        temp = nums[start] + nums[end]
        if temp == target:
            # print("{0}【{1}】, {2}【{3}】".format(start, nums[start], end, nums[end]))
            yield [start, end]
        end -= 1
        if start == end:
            start += 1
            end = len(nums) - 1


def sum_index2(nums, target):
    dic = {}
    for i, num in enumerate(nums):
        if num in dic:
            yield [dic[num], i]
        else:
            dic[target - num] = i


nums = range(0, 100)

start = time.time()
print([x for x in sum_index(nums)])
print('sum_index 耗时：', time.time() - start)

print('\n================================================\n')

start = time.time()
a = sum_index2(nums, 100)
print([x for x in a])
print('sum_index2 耗时：', time.time() - start)
