a = input().split()

a = [
  [1, 2, 3],
  [4, 5, 6]
]

nums = []
words = []
for i in a:
  try:
    n = int(i)
    nums.append(n)
  except Exception as e:
    words.append(i)


nums.extend(words)
print(nums)
# print(words)

