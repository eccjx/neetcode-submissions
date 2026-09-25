class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        sqr = defaultdict(set)
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == ".":
                    continue
                if num in row[i]:
                    return False
                else:
                    row[i].add(num)
                if num in col[j]:
                    return False
                else:
                    col[j].add(num)
                if num in sqr[(i // 3, j // 3)]:
                    return False
                else:
                    sqr[(i // 3, j // 3)].add(num)
        return True