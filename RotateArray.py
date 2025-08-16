class Solution:
    def rotateArr(self, arr: list, d: int) -> None:
        """
        Function to rotate an array by d elements in counter-clockwise direction.
        Modifies the array in-place.
        """
        n = len(arr)
        # Handle empty or single-element arrays, and unnecessary rotations
        if n <= 1 or d == 0:
            return

        # Normalize d to handle rotations greater than array length
        d = d % n

        # Helper function to reverse a portion of the array in-place
        def reverse(start, end):
            while start < end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1

        # Step 1: Reverse the first d elements
        reverse(0, d - 1)

        # Step 2: Reverse the remaining n-d elements
        reverse(d, n - 1)

        # Step 3: Reverse the entire array
        reverse(0, n - 1)

