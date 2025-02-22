class Solution1:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        M = len(mat1)
        K = len(mat1[0])
        N = len(mat2[0])
        output = [[0] * N for _ in range(M)]
        print(mat1, "\t", mat2, "\t", output)

        for i in range(M):
            for k in range(K):
                for n in range(N):
                    output[i][n] += mat1[i][k] * mat2[k][n]

        return output

class Solution2:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        def compress_matrix(matrix):
            rows, columns = len(matrix), len(matrix[0])
            cm = [[] for _ in range(rows)]

            for row in range(rows):
                for col in range(columns):
                    if matrix[row][col]:
                        cm[row].append([matrix[row][col], col])

            return cm

        matrix1 = compress_matrix(mat1)
        matrix2 = compress_matrix(mat2)

        M = len(mat1)
        K = len(mat1[0])
        N = len(mat2[0])

        output = [[0] * N for _ in range(M)]

        for mat1row in range(M):
            for ele1, mat1col in matrix1[mat1row]:
                for ele2, mat2col in matrix2[mat1col]:
                    output[mat1row][mat2col] += ele1 * ele2

        return output
