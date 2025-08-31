def binary_search(nums, target):
    left = 0
    right = len(nums)-1
    while left < right:
        mid = left + ((right - left)//2)
        if nums[mid] == target:
         return mid
        if target < nums[mid]:
            right = mid -1
        else:
            left = mid + 1
    return -1

print(binary_search([-1,0,3,5,9,12], 9))

print(binary_search([1,2,3,4,5], 4))


