def twosum(numbers, target):
    new_dict = dict()
    for i, number in enumerate(numbers):
        num = target - number
        if num in new_dict:
            return [new_dict[num], i]
        new_dict[number] = i
    return []


nums = [2, 3, 1, 6]
target = 9

sum = twosum(nums, target)
print(sum)
