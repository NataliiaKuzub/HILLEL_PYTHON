int_list = [int(i) for i in input('Please, enter the numbers, separated by comma: ').split(',')]
print(f'Sum of the entered numbers: {sum(int_list)} \n'
      f'Mean of the entered numbers: {sum(int_list)/len(int_list)} \n'
      f'Quantity of the even numbers for the given numbers: {len([i for i in int_list if i % 2 == 0])} \n'
      f'Quantity of the odd numbers for the given numbers: {len([i for i in int_list if i % 2 != 0])} \n'
      f'Minimum value for the given numbers: {min(int_list)} \n'
      f'Maximum value for the given numbers: {max(int_list)}')