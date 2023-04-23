arr1 = [1,2,3]
arr2 = [10,10,10]
# sum = 50 
arr1.sort()
arr2.sort()


n = len(arr1)
maxsum = 0
# for i in range(0, n):
#     maxsum += i * (arr2[i] - arr1[1])
arr1.reverse()
for i in range(1, n+1):
    maxsum += i * (arr2[i-1] - arr1[i-1])
print(maxsum)

# 1 * (10 - 1) = 9
# 2 * (10 - 2) = 16
# 3 * (10 - 3) = 21
#  = 46

# 1 * (10 - 3) = 7
# 2 * (10 - 2) = 16
# 3 * (10 - 1) = 27
