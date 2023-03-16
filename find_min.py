class FindMinimumInRotatedSortedArray():
    from typing import List

    def __init__(self, content = [66,26,46]):
        self.content = content
        print('>>', '\n', 'CONTENT : ',content)

    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums)-1
        while start <= end and nums[start] > nums[end]:
            m = end - start//2
            if nums[start] < nums[m]:
                start = m
            elif nums[start] > nums[m]:
                end = m - 1
            if nums[m] < nums[m-1]:
                return nums[m]
        return nums[start]
    
    def main(self):
        print('\033[92m',self.findMin(self.content), '\033[0m\n........')

# TEST :
if __name__ == '__main__':

    text = (
            [5,6,7,8,9,0,1,2,3,4],
            [2,3,4,5,6,7,8,9,0,1],
            [8,9,0,1,2,3,4,5,6,7],
            [6,7,8,9,0,1,2,3,4,5],
            [1,2,3,4,5,6,7,8,9,0],
            [3,4,5,6,7,8,9,0,1,2],
            [7,8,9,0,1,2,3,4,5,6],
            [4,1,2,3],
            [2,3,4,5],
            [5]
             )
             
    for item in text:
        FindMinimumInRotatedSortedArray(item).main()
