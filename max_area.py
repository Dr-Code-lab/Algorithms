class ContainerWithMostWater():
    from typing import List

    def __init__(self, content = [66,25,42]):
        self.content = content
        print('>>', '\n', 'CONTENT : ',content)

    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height)-1
        area = (end - start) * (height[start] - height[end])**2**0,5
        print("AREA: ", area)
        while start <= end:
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
            test = ((end - start) * (height[start] - height[end]))**2**0,5
            if test > area:
                area = test    
        return area
    
    def main(self):
        print('\033[92m',self.maxArea(self.content), '\033[0m\n........')

# TEST :
if __name__ == '__main__':

    text = (
            [1,8,6,2,5,4,8,3,7],
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
        ContainerWithMostWater(item).main()
