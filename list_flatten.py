# input: [1, [2], [[3]], [[[[4]], 5]], [[[[[6], 7]], 8]], [9]]
# output: [1, 2, 3, 4, 5, 6, 7, 8, 9]


def flatten_list(num):
    result = []

    for i in num:
        if type(i) == list:
            result.extend(flatten_list(i))
        else:
            result.append(i)

    return result


nums = [1, [2], [[3]], [[[[4]], 5]], [[[[[6], 7]], 8]], [9]]
res = flatten_list(nums)
print(res)
