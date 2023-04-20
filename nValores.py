nums = []
n = 1
i = 1
while n != 0:
  n = int(input(f'Número {i}: '))
  if n != 0:
    nums.append(n)
  i += 1

soma = 0
multi = 1
i = 0
while i <= len(nums) -1:
  soma += nums[i]

  if i != len(nums) - 1:
    print(nums[i], end=' + ')
  else:
    print(nums[i], ' = ', soma)

  i += 1

i = 0
while i <= len(nums) -1:
  multi *= nums[i]

  if i != len(nums) - 1:
    print(nums[i], end=' * ')
  else:
    print(nums[i], ' = ', multi)
  
  i += 1
