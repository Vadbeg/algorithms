from typing import Optional, List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        distance_mat = [[float("inf") for _ in range(len(mat[0]))] for _ in range(len(mat))]

        for curr_coord1 in range(len(mat)):
            for curr_coord2 in range(len(mat[0])):
                if mat[curr_coord1][curr_coord2] == 0:
                    distance_mat = self.run_distance_measuring(
                        coord1=curr_coord1,
                        coord2=curr_coord2,
                        mat=mat,
                        distance_mat=distance_mat,
                    )

        return distance_mat


    def run_distance_measuring(
        self,
        coord1: int,
        coord2: int,
        mat: List[List[int]],
        distance_mat: List[List[int]],
        curr_distance: int = 0
    ) -> List[List[int]]:
        distance_mat[coord1][coord2] = curr_distance

        if coord1 - 1 >= 0 and distance_mat[coord1 - 1][coord2] > curr_distance + 1 and mat[coord1 - 1][coord2] != 0:
            distance_mat = self.run_distance_measuring(
                coord1=coord1 - 1,
                coord2=coord2,
                mat=mat,
                distance_mat=distance_mat,
                curr_distance=curr_distance + 1
            )
        if coord1 + 1 < len(distance_mat) and distance_mat[coord1 + 1][coord2] > curr_distance + 1 and mat[coord1 + 1][coord2] != 0:
            distance_mat = self.run_distance_measuring(
                coord1=coord1 + 1,
                coord2=coord2,
                mat=mat,
                distance_mat=distance_mat,
                curr_distance=curr_distance + 1
            )
        if coord2 - 1 >= 0 and distance_mat[coord1][coord2 - 1] > curr_distance + 1 and mat[coord1][coord2 - 1] != 0:
            distance_mat = self.run_distance_measuring(
                coord1=coord1,
                coord2=coord2 - 1,
                mat=mat,
                distance_mat=distance_mat,
                curr_distance=curr_distance + 1
            )
        if coord2 + 1 < len(distance_mat[0]) and distance_mat[coord1][coord2 + 1] > curr_distance + 1 and mat[coord1][coord2 + 1] != 0:
            distance_mat = self.run_distance_measuring(
                coord1=coord1,
                coord2=coord2 + 1,
                mat=mat,
                distance_mat=distance_mat,
                curr_distance=curr_distance + 1
            )

        return distance_mat
