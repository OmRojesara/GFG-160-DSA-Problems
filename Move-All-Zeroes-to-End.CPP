class Solution {
public:
    void pushZerosToEnd(std::vector<int>& arr) {
        int nonZeroIndex = 0;
        // Iterate through the array
        for (int i = 0; i < arr.size(); i++) {
            // If the current element is non-zero,
            // place it at the next available nonZeroIndex
            if (arr[i] != 0) {
                arr[nonZeroIndex] = arr[i];
                nonZeroIndex++;
            }
        }

        // Now, all non-zero elements have been moved to the beginning.
        // Fill the remaining positions with zeros.
        while (nonZeroIndex < arr.size()) {
            arr[nonZeroIndex] = 0;
            nonZeroIndex++;
        }
    }
};
