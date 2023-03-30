# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0


class GuessNumberHigherOrLower():
    def __init__(self, content = [66], pattern = ''):
        self.content = content
        print('>>', '\n', 'CONTENT : ',content)

    def guess(self, num: int) -> int:
        if num > self.content:
            return -1
        elif num < self.content:
            return 1
        return 0


    def guessNumber(self, n: int) -> int:
        max = n
        min = 0
        while min < max:
            mean_int = (min + max)//2
            guess_return = self.guess(mean_int)
            if guess_return == -1:
                min = mean_int
            elif guess_return == 1:
                max = mean_int
            else:
                return mean_int

    
    def main(self):
        print('\033[92m',self.guessNumber(self.content), '\033[0m\n........')

# TEST :
if __name__ == '__main__':

    text = (
            5,6,7,8,9,0,1,2,3,4,23,45,67,89,11,
             )
             
    for item in text:
        GuessNumberHigherOrLower(item).main()
