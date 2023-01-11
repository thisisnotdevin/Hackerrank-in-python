# O(n^2) solution
def formingMagicSquare(s):
    # must have 5 in the middle, and the sum of any line is 15
    # all possible combinations IN A TRIPLE ARRAY!
    magicSquares = [[[8, 1, 6], [3, 5, 7], [4, 9, 2]],
                     [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
                     [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
                     [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
                     [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
                     [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
                     [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
                     [[2, 7, 6], [9, 5, 1], [4, 3, 8]]]
                     
    # set infinity to compare values later          
    minCost = float('inf') 
    
    for i in range(8):
        # reset cost to 0
        cost = 0
        for j in range(3):
            for k in range(3):
                # comparing each group to find the difference and adding it to cost
                cost += abs(s[j][k] - magicSquares[i][j][k])
                
        # comparning to current minCost and setting a new one if lower        
        minCost = min(minCost, cost)
    return minCost
    
