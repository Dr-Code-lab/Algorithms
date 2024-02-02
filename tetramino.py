import sys


def read_map_from_user_input() -> str:
    counter = 0
    map_string: str = ""
    print("Please input map 8x8:")
    for i in sys.stdin:
        map_string += i + "\n"
        counter += 1
        if counter == 8:
            break
    return map_string


def read_map_from_file() -> str:
    with open("input.txt", "r") as map_file:
        map_content: str = map_file.read()
        return map_content


def shape_map(map_string: str) -> list[list[str]]:
    map_list: list[str] = map_string.split()
    if len(map_list) != 8:
        sys.stderr.write('Exception! Bad size map!')
        exit()
    map_2d: list[list[str]] = list()
    for string in map_list:
        map_2d.append(list(string.replace("\\n", "")))
        if len(map_2d[-1]) != 8:
            sys.stderr.write('Exception! Bad size line in map!')
            exit()
    return map_2d


class TetraminoPositionCounter:

    def __init__(self):
        if "input.txt" in sys.argv:
            tetris_map: str = read_map_from_file()
        else:
            tetris_map: str = read_map_from_user_input()

        self.shaped_map: list[list[str]] = shape_map(tetris_map)
        self.result: int = 0

    def search_space_around(self, line_id: int, place_id: int):
        if line_id < 7:
            if place_id < 6:
                if (self.shaped_map[line_id][place_id + 1] == '.'
                        and self.shaped_map[line_id][place_id + 2] == '.'
                        and self.shaped_map[line_id + 1][place_id + 1] == '.'):
                    self.result += 1
            if place_id < 7:
                if (self.shaped_map[line_id + 1][place_id - 1] == '.'
                        and self.shaped_map[line_id + 1][place_id] == '.'
                        and self.shaped_map[line_id + 1][place_id + 1] == '.'):
                    self.result += 1
            if line_id < 6:
                if place_id < 7:
                    if (self.shaped_map[line_id + 1][place_id] == '.'
                            and self.shaped_map[line_id + 1][place_id + 1] == '.'
                            and self.shaped_map[line_id + 2][place_id] == '.'):
                        self.result += 1
                if (self.shaped_map[line_id + 1][place_id - 1] == '.'
                        and self.shaped_map[line_id + 1][place_id] == '.'
                        and self.shaped_map[line_id + 2][place_id] == '.'):
                    self.result += 1

    def check_map(self):
        for line_id, line in enumerate(self.shaped_map):
            for place_id, place in enumerate(line):
                if place == '.':
                    self.search_space_around(line_id, place_id)
                elif place == '*':
                    continue
                else:
                    sys.stderr.write('Exception! Wrong symbol in map!')
                    exit()

    def main(self):
        self.check_map()
        if "output.txt" in sys.argv:
            with open("output.txt", 'w', encoding="utf-8") as file_result:
                file_result.write(str(self.result))
        else:
            sys.stdout.write(str(self.result))


if __name__ == '__main__':
    TetraminoPositionCounter().main()
