class Solution:
    def maxProfit(self, prices: List[int]) -> int:



        #Using two pointers method set pointer "buy" on first element
        #and pointer sell on second element of our prices array.
        buy, sell = 0, 1



        #Declare the max profit variable to determine, if profit is the 
        #max profit
        maxProfit = 0


        #looping through until sell pointer reaches the edge of the array
        while sell < len(prices):
            #If we have the profit, calculate the profit and check if it's
            #bigger than our current maxProfit. If transaction is not profitable
            #increment our Sell pointer by 1, to check next value.
            if(prices[buy] < prices[sell]):
                profit = prices[sell] - prices[buy]
                maxProfit = max(maxProfit, profit)
            else:



                #If selling point is the new lowest point, update the buy pointer
                #to shows the new lowest point. Buy = Sell
                buy = sell
            sell += 1

        #returning the max profit    
        return maxProfit