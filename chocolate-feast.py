    
Solution 1:
  def chocolateFeast(n, c, m):
    chochoAte = n // c  # int division
    wrappers = chochoAte
    
    while wrappers >= m:
        wrappers = wrappers - m
        chochoAte += 1
        wrappers += 1
    return int(chochoAte)
    
    
    
Solution 2:
  def chocolateFeast(n, c, m):
    chochoAte = n // c  # integer division
    wrappers = chochoAte
    
    # calculate the total number of chocolates that can be obtained
    total_choco = chochoAte
    while wrappers >= m:
        new_choco = wrappers // m
        total_choco += new_choco
        wrappers = (wrappers % m) + new_choco
    
    return total_choco
