class Solution:
    def nextPermutation(self, arr):
        n = len(arr)

        # Step 1: Find the break-point (pivot)
        i = n - 2
        while i >= 0 and arr[i] >= arr[i + 1]:
            i -= 1

        # If no break-point found, reverse the entire array
        if i == -1:
            arr.reverse()
            return arr

        # Step 2: Find the successor
        j = n - 1
        while arr[j] <= arr[i]:
            j -= 1

        # Step 3: Swap pivot and successor
        arr[i], arr[j] = arr[j], arr[i]

        # Step 4: Reverse the suffix
        left = i + 1
        right = n - 1
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

        return arr

