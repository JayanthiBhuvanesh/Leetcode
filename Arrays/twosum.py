def two_sum(nums, target):
    target_list = []
    for i in range(len(nums)-1):
        for j in range(1, len(nums)-1):
            if nums[i] + nums[j] == target:
                target_list.append(i)
                target_list.append(j)
    return target_list

print(two_sum([2,7,11,15], 9))

