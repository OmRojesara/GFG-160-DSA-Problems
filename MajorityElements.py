class Solution:
    def findMajority(self, arr):
        n = len(arr)
        if n == 0:
            return []

        # Candidate Selection Phase
        candidate1, candidate2 = 0, 1 # Initialize with distinct values to handle edge cases
        count1, count2 = 0, 0

        for num in arr:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1 = num
                count1 = 1
            elif count2 == 0:
                candidate2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1

        # Validation Phase
        final_count1, final_count2 = 0, 0
        for num in arr:
            if num == candidate1:
                final_count1 += 1
            elif num == candidate2:  # Use elif to avoid double counting if candidate1 == candidate2
                final_count2 += 1

        result = []
        if final_count1 > n // 3:
            result.append(candidate1)
        # Ensure candidate2 is different from candidate1 before adding, to avoid duplicates if they happen to be the same
        if candidate1 != candidate2 and final_count2 > n // 3:
            result.append(candidate2)
        elif candidate1 == candidate2 and final_count1 > n // 3: # If they are the same candidate, already added
            pass
        elif candidate1 != candidate2 and final_count2 > n // 3: # Redundant check, but good for clarity
            result.append(candidate2)


        result.sort() # Sort the results as per problem requirement
        return result

