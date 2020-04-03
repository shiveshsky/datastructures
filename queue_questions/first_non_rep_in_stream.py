class Solution:
    def solve(self, A):
        queue = []
        ans = ""
        freq_map = {}
        for i in A:
            if len(queue) > 0 and i == queue[0]:
                freq_map[i]+=1
                queue.pop(0)
                if len(queue) == 0:
                    ans += "#"
                else:
                    while freq_map[queue[0]] > 1:
                        queue.pop(0)
                    if len(queue)>0:
                        ans += queue[0]
                    else:
                        ans+="#"
            else:
                if i in freq_map:
                    freq_map[i] += 1
                    if len(queue)>0:
                        while freq_map[queue[0]]>1:
                            queue.pop(0)
                        ans += queue[0]
                    elif len(queue)==0:
                        ans += "#"
                else:
                    freq_map[i] = 1
                    queue.append(i)
                    ans += queue[0]

        return ans

print(Solution().solve("aabbcbbca"))  # >aabbddc#####
