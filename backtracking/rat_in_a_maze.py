class Solution:
    def unique_paths(self, A):
        start = [0,0]
        all_zeros = 0
        for i in range(0, len(A)):
            for j in range(0, len(A[0])):
                if A[i][j]==0:
                    all_zeros+=1
                if A[i][j]==1:
                    start[0]=i
                    start[1]=j
        path_cnt = 0
        ans = [0]
        A[start[0]][start[1]]=-1
        self.moon_walker(start, all_zeros, A, [], ans)
        A[start[0]][start[1]] = 1
        return ans

    def is_walkable(self, location, A):
        if location[0]<0 or location[0]>=len(A):
            return False
        if location[1]<0 or location[1]>=len(A[0]):
            return False
        if A[location[0]][location[1]]==-1:
            return False
        return True

    def moon_walker(self, start, total_zeros, A, path, ans):
        if A[start[0]][start[1]]==2:
            if len(path) == total_zeros+1:
                ans[0]+=1
            return
        dirs = 'UDLR'
        for dir in dirs:
            if dir == 'U':
                location = [start[0]-1, start[1]]
                if self.is_walkable(location, A):
                    path.append(location)
                    old_val = A[location[0]][location[1]]
                    if old_val == 0:
                        A[location[0]][location[1]] = -1
                    self.moon_walker([start[0]-1, start[1]], total_zeros, A, path, ans)
                    path.pop()
                    if old_val == 0:
                        A[location[0]][location[1]] = 0
            if dir == 'D':
                location = [start[0]+1, start[1]]
                if self.is_walkable(location, A):
                    path.append(location)
                    old_val = A[location[0]][location[1]]
                    if old_val==0:
                        A[location[0]][location[1]] = -1
                    self.moon_walker([location[0], location[1]], total_zeros, A, path, ans)
                    path.pop()
                    if old_val==0:
                        A[location[0]][location[1]] = 0
            if dir == 'L':
                location =[start[0], start[1]-1]
                if self.is_walkable(location, A):
                    path.append(location)
                    old_val = A[location[0]][location[1]]
                    if old_val == 0:
                        A[location[0]][location[1]] = -1
                    self.moon_walker([location[0], location[1]], total_zeros, A, path, ans)
                    path.pop()
                    if old_val==0:
                        A[location[0]][location[1]] = 0
            if dir == 'R':
                location = [start[0], start[1] + 1]
                if self.is_walkable(location, A):
                    path.append(location)
                    old_val = A[location[0]][location[1]]
                    if old_val == 0:
                        A[location[0]][location[1]] = -1
                    self.moon_walker([location[0], location[1]], total_zeros, A, path, ans)
                    path.pop()
                    if old_val==0:
                        A[location[0]][location[1]] = 0
