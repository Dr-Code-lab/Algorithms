class FindAllAnagramsInString():
    from typing import List

    def __init__(self, content = [66,26,46], pattern = ''):
        self.content = content
        print('>>', '\n', 'CONTENT : ',content)

    def findAnagrams(self, s: str, p: str) -> List[int]:
        def hashing(string, hash_map):
            for char in string:
                if not hash_map.get(char):
                    hash_map[char] = 1
                else:
                    hash_map[char]+=1
            return hash_map
        
        if s == p:
            return[0]
        size = len(s)
        frame_size = len(p)
        if frame_size > size:
            return
        start = 0
        end = frame_size - 1
        list_ids = []
        hash_p = hashing(p, {})
        hash_s = None
        while end < size:
            window = s[start:start+frame_size]
            if not hash_s:
                hash_s = hashing(window, {})
            else:
                hash_s = hashing(window[-1], hash_s)
            if hash_p == hash_s:
                list_ids.append(start)
            hash_s[window[0]]-=1
            if hash_s.get(window[0]) == 0:
                hash_s.pop(window[0])
            start+=1
            end+=1
        return list_ids

    
    def main(self):
        pattern = 'abc'
        print('\033[92m',self.findAnagrams(self.content, pattern), '\033[0m\n........')

# TEST :
if __name__ == '__main__':

    text = (
            'baceabcaracba',
            'cbecbaahuyabcaabacb',
            '',
            'a'
             )
             
    for item in text:
        FindAllAnagramsInString(item).main()
