class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            duplicateHash = {}
            for j in range(9):
                key = board[i][j]
                duplicateHash[key] =  duplicateHash.get(key, 0) + 1
                if key != '.' and duplicateHash[key] == 2: return False
        for j in range(9):
            duplicateHash = {}
            for i in range(9):
                key = board[i][j]
                duplicateHash[key] =  duplicateHash.get(key, 0) + 1
                if key != '.' and duplicateHash[key] == 2: return False
        for boxRow in range(0, 9, 3):
            for boxCol in range(0, 9, 3):
                duplicateHash = {} 
                for i in range(boxRow, boxRow + 3, 1):
                    for j in range(boxCol, boxCol + 3, 1):
                        key = board[i][j]
                        duplicateHash[key] =  duplicateHash.get(key, 0) + 1
                        if key != '.' and duplicateHash[key] == 2: return False
        return True
        
            

        