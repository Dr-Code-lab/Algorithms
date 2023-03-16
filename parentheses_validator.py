class ParenthesesValidator():
    from typing import List

    def __init__(self, content = '( init string)', fix = False):
            self.content = content
            self.fix = fix
            print('>>', '\n', 'CONTENT : ',content)


    def isValid(self,s: str) -> bool:
        keys = [')', ']', '}']
        values =['(', '[', '{']
        parentheses = {key:value for key,value in zip(keys,values)}
        stack_operations = []
        for char in s:
            if char in parentheses.values():
                stack_operations.append(char)
            elif (not stack_operations 
                  or not stack_operations[-1] == parentheses.get(char)):
                return False
            elif stack_operations[-1] == parentheses.get(char):
                stack_operations.pop(-1)
        if not stack_operations:
            return True
        return False

    def main(self):
        if self.isValid(self.content):
            print('\033[92m',self.isValid(self.content), '\033[0m\n........')
        else:
            print('\033[91m',self.isValid(self.content), '\033[0m\n........')

# TEST :
if __name__ == '__main__':

    text = (
            '(){}[]',                                       # True
            ']',                                            # False
            '(])',                                          # False
            '{',                                            # False
            '(}',                                           # False
            '([{()(){[)[}{{}}{{{}}}]]}]})',                 # False
            '(({[[[[[[{{{{{}[][()]}}}}]]]]]}]))',           # False
            '([{[([{()()}{[[[[{}{}{}][()()()]]]]}])]}])',   # True
             )
             
    for string in text:
        ParenthesesValidator(string, True).main()
