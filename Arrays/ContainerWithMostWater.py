from typing import List

class solution:
    def maxArea(self, height: List[int]) -> int:
        max_left, max_right =0, 0
        left =0
        right = len(height) -1

        while left < right:
            max_left = max(max_left, height[left])
            max_right = max(max_right, height[right])
            left+=1
            right-=1


        return min(max_right, max_left) * min(max_right, max_left)

solver = solution()
height_list = [1,8,6,2,5,4,8,3,7]
print(solver.maxArea(height_list))