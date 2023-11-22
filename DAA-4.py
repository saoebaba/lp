def solve_knapsack():
    val = [10,10,12,18] 
    wt = [2,4,6,9] 
    W = 15
    n = len(val) - 1
    def knapsack(W, n): 
    
         if n < 0 or W <= 0:
             return 0
 
         if wt[n] > W:
             return knapsack(W, n - 1)
         else:
            return max(val[n] + knapsack(W - wt[n], n - 1), knapsack(W, n - 1))
    print(f'Maximumu value of item that can be carried : {knapsack(W, n)}')
solve_knapsack()
