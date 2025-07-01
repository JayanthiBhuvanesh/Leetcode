#brute force
def two_sum(nums, target):
    target_list = []
    for i in range(len(nums)-1):
        for j in range(1, len(nums)-1):
            if nums[i] + nums[j] == target:
                target_list.append(i)
                target_list.append(j)
    return target_list


print(two_sum([2,7,11,15], 9))

#Hash map

def two_sum_using_map(nums, target):
    target_map = {}
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in target_map:
            return (target_map[diff], i)
        target_map[nums[i]] = i
    return []

print(two_sum_using_map([2, 7, 11,15], 9))

#Approach
# 1. Iterate through each element
# 2. Store the index of the element for each element in a hash map
# 3. check if the difference of element is in the map, if so return the index of the current element and the index of the difference