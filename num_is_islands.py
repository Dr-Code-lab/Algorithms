class CountIslands():
    from typing import List
    def __init__ (self, content = [[1,2,3],[4,5,6],[7,8,9]]):
        self.content = content
        print(content, '\n')

    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(row, column):
            if row < 0 or column < 0 or row == rows or column == columns:
                return
            if grid[row][column] != '1':  # There is land
                return

            grid[row][column] = '*' # Mark visited lands
            dfs(row-1, column)
            dfs(row+1, column)
            dfs(row, column+1)
            dfs(row, column-1)            
          
        num_of_isls = 0
        rows = len(grid)
        columns = len(grid[0])

        for row in range(rows):
            for column in range(columns):
                if grid[row][column] == '1':
                    dfs(row, column)
                    num_of_isls += 1

        return num_of_isls

    
    def main(self):
        result = self.numIslands(self.content)
        if result:
            print('\033[92m',result, '\033[0m\n........')
        else:
            print('\033[91m',result, '\033[0m\n........')

    # TEST :
if __name__ == '__main__':

    args = (
            [["0","1","1","1","0"],
             ["1","0","0","1","0"],
             ["1","1","0","0","0"],
             ["0","0","0","0","0"]],

            [["1","1","1","1","0"],
             ["1","1","0","1","0"],
             ["1","1","0","0","0"],
             ["0","0","0","0","0"]],

            [["1","1","0","0","0"],
             ["1","1","0","0","0"],
             ["0","0","1","0","0"],
             ["0","0","0","1","1"]],

            [["0","1","0","0","1"],
             ["1","0","0","0","0"],
             ["0","0","1","0","0"],
             ["0","0","0","1","1"]]
            )
             
    for item in args:
        CountIslands(item).main()
