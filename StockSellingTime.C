// User function Template for C
#include <limits.h> // Required for INT_MAX if used, though a simpler approach avoids it

int maximumProfit(int prices[], int pricesSize) {
    // Handle edge case: if there are less than 2 days, no transaction is possible.
    if (pricesSize <= 1) {
        return 0; 
    }

    // Initialize minPrice with the first day's price
    int minPrice = prices[0]; 
    // Initialize maxProfit to 0, as profit can't be negative in this problem
    int maxProfit = 0; 

    // Iterate through the prices starting from the second day
    for (int i = 1; i < pricesSize; i++) {
        // Calculate the potential profit if sold on the current day
        int currentProfit = prices[i] - minPrice;
        
        // Update maxProfit if the current profit is greater
        if (currentProfit > maxProfit) {
            maxProfit = currentProfit;
        }

        // Update minPrice if a lower buying price is found
        if (prices[i] < minPrice) {
            minPrice = prices[i];
        }
    }

    // Return the calculated maximum profit
    return maxProfit;
}
