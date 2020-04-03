class Solution:
    element_freq = {}
    freq_element = {}
    max_freq = 0

    def __init__(self):
        self.element_freq = dict()
        self.freq_element = dict()

    def solve(self, A):
        ans = []

        for ele in A:
            ans.append(self.push_to_stack(ele[1]) if ele[0] == 1 else self.pop_most_freq())
        return ans

    def push_to_stack(self, x):
        if x not in self.element_freq:
            self.element_freq[x] = 1
        else:
            self.element_freq[x] += 1
        self.max_freq = max(self.max_freq, self.element_freq[x])
        if self.element_freq[x] not in self.freq_element:
            self.freq_element[self.element_freq[x]] = []
        self.freq_element[self.element_freq[x]].append(x)
        return -1

    def pop_most_freq(self):
        top = self.freq_element[self.max_freq][-1]
        self.freq_element[self.max_freq].pop()

        self.element_freq[top]-=1

        if len(self.freq_element[self.max_freq])==0:
            self.max_freq-=1
        return top

print(Solution().solve([
            [1, 5],
            [1, 7],
            [1, 5],
            [1, 7],
            [1, 4],
            [1, 5],
            [2, 0],
            [2, 0],
            [2, 0],
            [2, 0]  ]))