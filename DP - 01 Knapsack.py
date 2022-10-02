#01 knapsack problem
'''
Suppose you are a thief with a knapsack which can carry 8kg of goods. You have 4 items that you can put in the knapsack:        laptop that weighs 2kg and costs $1000, a chunk of gold that weighs 3kg and costs $2000, a diamond that weighs 4kg and costs    $5000 and a gold phone that weighs 5kg and costs $6000. Which items should you steal so that you steal the maximum moneys worth  of goods?

A more general example would be: Suppose you are a thief with a knapsack which can carry a certain weight of goods. You have n items which have a certain weight and cost that you can put in the knapsack. Which items should you steal so that you steal the maximum moneys worth of goods?
'''

#Explanation & Solution
'''
The simple solution is to try every possible set of goods and find the set that gives you the most value. However this is very slow and takes exponential time. So how can you get the answer faster? With Dynamic Programming! 

Grid after filling:
      1  2     3     4     5     6     7     8
[2[0, 0, 1000, 1000, 1000, 1000, 1000, 1000, 1000], 
 3[0, 0, 1000, 2000, 2000, 3000, 3000, 3000, 3000], 
 4[0, 0, 1000, 2000, 5000, 5000, 6000, 7000, 7000], 
 5[0, 0, 1000, 2000, 5000, 6000, 6000, 7000, 8000]]
'''
def knapsack01(weights, costs, size):
    dp = [[0] * (size + 1) for i in range(len(costs))]
    for i in range(len(dp)):
        for j in range(len(dp[0])):
            if i == 0 and j < weights[i]:
               dp[i][j] = 0
            if j < weights[i]:
               dp[i][j] = dp[i - 1][j]
            else:
               dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weights[i]] + costs[i])
    return dp
print(knapsack01([2, 3, 4, 5], [1000, 2000, 5000, 6000], 8))
