nums = list()

while True:
    num = input('Enter a number: ')
    nums.append(num)
    if num == 'done': break
        
nums.remove('done')
print('Minimum:',min(nums))
print('Maximum:',max(nums))