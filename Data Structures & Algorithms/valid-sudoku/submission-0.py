class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        '''
        make a set for rows and cols, do a map for swaure where swaure coord is key and val is set

        make sets and map before, looping (list of sets lets u index the list and access that set like that)

        loop through grid:
            if element is '.' continue 
            else if in set return false 
            else add to set and continue

        end of loop return true

        check square by doing // by 3 for each index
        '''

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        squares = {}

        for r in range(9):
            for c in range(9):
                e = board[r][c]
                if e == '.':
                    continue
                
                square = squares.setdefault((r // 3, c // 3), set())
                if e in rows[r] or e in cols[c] or e in square:
                    return False

                rows[r].add(e)
                cols[c].add(e)
                square.add(e)
        
        return True



        

                