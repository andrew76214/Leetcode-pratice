class Solution:
    def merge(self, arr, left, mid, right):
        n1 = mid - left + 1
        n2 = right - mid

        # Create temp arrays
        L = [0] * n1
        R = [0] * n2

        # Copy data to temp arrays L[] and R[]
        for i in range(n1):
            L[i] = arr[left + i]
        for j in range(n2):
            R[j] = arr[mid + 1 + j]

        i = 0  # Initial index of first subarray
        j = 0  # Initial index of second subarray
        k = left  # Initial index of merged subarray

        # Merge the temp arrays back
        # into arr[left..right]
        while i < n1 and j < n2:
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Copy the remaining elements of L[],
        # if there are any
        while i < n1:
            arr[k] = L[i]
            i += 1
            k += 1

        # Copy the remaining elements of R[], 
        # if there are any
        while j < n2:
            arr[k] = R[j]
            j += 1
            k += 1

    def merge_sort(self, arr, left, right):
        if left < right:
            mid = (left + right) // 2

            self.merge_sort(arr, left, mid)
            self.merge_sort(arr, mid + 1, right)
            self.merge(arr, left, mid, right)
    
    def maxOperations(self, nums: List[int], k: int) -> int:
        # Sorting
        self.merge_sort(nums, 0, len(nums) - 1)

        # Count
        left_index = 0
        right_index = len(nums) - 1
        count = 0

        while left_index < right_index:
            if (nums[left_index] + nums[right_index]) == k:
                count += 1
                left_index += 1
                right_index -= 1
            elif ((k - nums[right_index]) > nums[left_index]):
                left_index += 1
            else:
                right_index -= 1
            
        return count
