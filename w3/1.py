'''
3
1 2 3
4 5 6
7 8 9
'''
n = int(input())
arr = []
for i in range(n):
  nums = list(map(float, input().split()))
  arr.append(nums)


print(arr[1][2])

# for i in range(len(arr)):
#   print(arr[i])
