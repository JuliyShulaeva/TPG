import numpy as np

matrix = np.array([[5, 7, 8, 6, 1], [9, 1, 2, 3, 4],[0, 4, 7, 8, 3],[2, 8, 9, 7, 3],[3, 0, 1, 4, 7]], dtype=np.float)
print('matrix = ', matrix)

p1 = len(matrix)
#print('p1 = ', p1)

unit_matrix = np.eye(p1)
print('unit_matrix = ', unit_matrix)

reverse_matrix = matrix * unit_matrix
print('reverse_matrix = ', reverse_matrix)

reverse_reverse_matrix = reverse_matrix * unit_matrix
print('reverse_reverse_matrix = ', reverse_reverse_matrix)

jordanova_form = matrix * reverse_matrix * reverse_reverse_matrix
print('jordanova_form = ', jordanova_form)
