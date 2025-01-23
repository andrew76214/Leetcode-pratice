class Solution:
    def maxArea(self, height: List[int]) -> int:
        left_index = 0
        right_index = len(height) - 1
        max_water = 0

        while (left_index != right_index):
            current_water = 0
            if height[left_index] > height[right_index]:
                current_water = height[right_index] * (right_index - left_index)
                right_index -= 1
            else:
                current_water = height[left_index] * (right_index - left_index)
                left_index += 1

            if current_water > max_water:
                max_water = current_water

        return max_water
