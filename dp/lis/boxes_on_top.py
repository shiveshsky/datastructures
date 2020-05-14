class Box:
    def __init__(self, height=0, breadth=0, length=0):
        self.height = height
        self.breadth = breadth
        self.length = length

    def __lt__(self, other):
        return (self.breadth*self.length) < (other.breadth*other.length)


class Solve:
    def solve(self, boxes):
        rotations = [Box() for _ in range(3*len(boxes))]
        i = 0
        ind = 0
        while i < len(rotations):
            rotations[i].height = boxes[ind].height
            rotations[i].length = max(boxes[ind].length, boxes[ind].breadth)
            rotations[i].breadth = min(boxes[ind].length, boxes[ind].breadth)
            i+=1
            rotations[i].height = boxes[ind].length
            rotations[i].length = max(boxes[ind].height, boxes[ind].breadth)
            rotations[i].breadth = min(boxes[ind].height, boxes[ind].breadth)
            i += 1
            rotations[i].height = boxes[ind].breadth
            rotations[i].length = max(boxes[ind].height, boxes[ind].length)
            rotations[i].breadth = min(boxes[ind].height, boxes[ind].length)
            i += 1
            ind += 1
        rotations.sort(reverse=True)
        dp = [box.height for box in rotations]

        for i in range(0, len(rotations)):
            for j in range(i - 1, -1, -1):
                if rotations[i].breadth < rotations[j].breadth and rotations[i].length < rotations[j].length:
                    dp[i] = max(dp[i], rotations[i].height + dp[j])
        return max(dp)


if __name__ == '__main__':
    arr = [Box(4, 6, 7), Box(1, 2, 3),
           Box(4, 5, 6), Box(10, 12, 32)]  # ans = 60
    print(Solve().solve(arr))