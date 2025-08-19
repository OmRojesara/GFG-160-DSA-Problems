class Solution:
    def getMinDiff(self, arr, k):
        # Sort the array to easily identify potential minimum and maximum elements.
        arr.sort() 
        n = len(arr)
        
        # Initialize the minimum difference with the difference between the
        # largest and smallest elements before any modifications.
        ans = arr[n-1] - arr[0] 
        
        # Iterate through the array to consider all possible "split points"
        # where modifications might be applied.
        for i in range(1, n):
            # If subtracting 'k' from the current element would result in a negative height,
            # applying -k is not possible.
            if arr[i] - k < 0:
                continue 
            
            # Calculate the potential new minimum height.
            min_height = min(arr[0] + k, arr[i] - k) 
            
            # Calculate the potential new maximum height.
            max_height = max(arr[i-1] + k, arr[n-1] - k) 
            
            # Update the overall minimum difference found so far.
            ans = min(ans, max_height - min_height) 
            
        return ans
