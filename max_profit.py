class BestTimeToBuyAndSellStock():
    from typing import List

    def __init__(self, content = [66,25,42]):
        self.content = content
        print('>>', '\n', 'CONTENT : ',content)

    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        profit = 0
        min_buy = prices[0]
        for price in prices:
            if price > min_buy:
                if price - min_buy > profit:
                    profit = price - min_buy
            else:
                min_buy = price
        return profit
    
    def main(self):
        print('\033[92m',self.maxProfit(self.content), '\033[0m\n........')

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
            [0],
            [],
            [5],
            [1,1]
             )
             
    for item in text:
        BestTimeToBuyAndSellStock(item).main()
