class Solution:
    def coordinates_to_idx(self, i, j):
        return (i * self.row_len) + j
    def idx_to_coordinates(self, idx):
        return [idx // self.row_len, idx % self.row_len]
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        self.row_len = len(matrix[0])
        lo = 0
        hi = len(matrix) * len(matrix[0]) - 1
        while lo <= hi:
            mid = self.idx_to_coordinates((lo + hi) // 2)
            if matrix[mid[0]][mid[1]] == target:
                return True
            if matrix[mid[0]][mid[1]] < target:
                lo = self.coordinates_to_idx(mid[0], mid[1]) + 1
            else:
                hi = self.coordinates_to_idx(mid[0], mid[1]) - 1
        return False
        # lo = [0, 0]
        # hi = [len(matrix) - 1, len(matrix[0]) - 1]
        # while lo[0] <= hi[0] and lo[1] <= hi[1]:
        #     mid = [(lo[0] + hi[0]) // 2, (lo[1] + hi[1]) // 2 ]

        #     print("lo idx: ", lo, " lo val: ", matrix[lo[0]][lo[1]])
        #     print("mid idx: ", mid, " mid val: ", matrix[mid[0]][mid[1]])
        #     print("hi idx:", hi, " hi val: ", matrix[hi[0]][hi[1]])

        #     if matrix[mid[0]][mid[1]] == target:
        #         return True
        #     if matrix[mid[0]][mid[1]] < target:
        #         if mid[1] < len(matrix[0]) - 1:
        #             lo[0] = mid[0]
        #             lo[1] = mid[1] + 1
        #         else:
        #             lo[0] = mid[0] + 1
        #             lo[1] = 0
        #     else:
        #         if mid[1] > 0:
        #             hi[0] = mid[0]
        #             hi[1] = mid[1] - 1
        #         else:
        #             hi[0] = mid[0] - 1
        #             hi[1] = len(matrix[0]) - 1
        # return False
        