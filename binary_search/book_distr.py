class Solve:

    def book_feasibility(self, A, max_min_pages, students):
        i = 0
        pages_given = 0
        while i < len(A) and students > 0:
            pages_given += A[i]
            if pages_given <= max_min_pages:
                i += 1
            else:
                students -= 1
                pages_given = 0
        if i < len(A):
            return False
        else:
            students -= 1
        return True

    def books(self, A, B):
        search_space_l = max(A)
        search_space_h = sum(A)
        ans = 999999999
        while search_space_l <= search_space_h:
            search_space_m = (search_space_l + search_space_h) // 2
            pages_feasibility = self.book_feasibility(A, search_space_m, B)
            if pages_feasibility:
                ans = min(ans, search_space_m)
                search_space_h = search_space_m - 1
            else:
                search_space_l = search_space_m + 1

        return ans


print(Solve().books([12, 34, 67, 90], 2))
