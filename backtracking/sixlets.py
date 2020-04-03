class Sixlets:

    def sixlets(self, A, B):
        A.sort()
        ans_cnt = [0]
        self.sixletsolver(A, B, 1000, 0, 0, ans_cnt)
        return ans_cnt[0]

    def sixletsolver(self, A, B, req_sum, current_sum, current_size, ans_cnt):
        if current_sum > req_sum:
            return
        if current_sum<=req_sum:
            if current_size==B:
                ans_cnt[0]+=1
                return

        for i in range(0, len(A)):
            current_sum += A[i]
            if current_sum <= req_sum:
                self.sixletsolver(A[i+1:], B, req_sum , current_sum, current_size+1, ans_cnt)
            current_sum -= A[i]
