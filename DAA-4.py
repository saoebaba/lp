def solve_knapsack():
    val = [12,45,60,13] 
    wt = [5,3,2,10] 
    W = 22
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
