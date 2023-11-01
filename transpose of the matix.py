matrix=[
    [4,6,7,8],
    [3,7,2,7],
    [7,3,7,5]
    ]
transposed_matrix=[[row[i]for row in matrix]for i in range(len(matrix[0]))]
for row in transposed_matrix:
    print(row)
