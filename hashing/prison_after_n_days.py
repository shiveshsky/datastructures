'''https://www.youtube.com/watch?v=secuBlDy0YQ&feature=youtu.be'''


class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        seen = set()
        flag = False
        size = 0
        for j in range(0, N):
            new_cells = [0] * 8
            for i in range(1, 7):
                if cells[i - 1] == cells[i + 1]:
                    new_cells[i] = 1
                else:
                    new_cells[i] = 0

            if "".join(map(str, new_cells)) not in seen:
                size += 1
                seen.add("".join(map(str, new_cells)))
            else:
                flag = True
                break
            cells = new_cells
        if flag:
            N = N % size
            for j in range(0, N):
                new_cells = [0] * 8
                for i in range(1, 7):
                    if cells[i - 1] == cells[i + 1]:
                        new_cells[i] = 1
                    else:
                        new_cells[i] = 0

                cells = new_cells
        return cells
