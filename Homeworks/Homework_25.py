def rotate_matrix(source_matrix):
    new_matrix = []
    for col in range(4):
        new_row = [source_matrix[row][col] for row in range(2, -1, -1)]
        new_matrix.append(new_row)
    return new_matrix


matrix = []

for n in range(1, 4):
    element = [int(i) for i in input(f'Please, data for the row #{n}: ').split(',')]
    if len(element) == 4:
        matrix.append(element)
    else:
        print('Entry is incorrect. Please, try one more time.')
        break

for i in rotate_matrix(matrix):
    print(' '.join([str(k) for k in i]))
