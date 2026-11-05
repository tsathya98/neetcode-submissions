class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rset = defaultdict(set)
        cset = defaultdict(set)
        bset = defaultdict(set)
        for r in range(len(board)):
            for c in range(len(board[0])):
                val = board[r][c]
                if val == ".":
                    continue
                b = (r//3,c//3)
                if val in rset[r] or val in cset[c] or val in bset[b]:
                    return False
                rset[r].add(val)
                cset[c].add(val)
                bset[b].add(val)
        return True