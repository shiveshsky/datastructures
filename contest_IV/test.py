def merge(common, row):
    i=0
    j=0
    merged = []
    if len(common)==0:
        return row
    while i<len(common) and j<len(row):
        if common[i]==row[j]:
            merged.append(common[i])
            i+=1
            j+=1
        elif common[i]<row[j]:
            i+=1
        elif common[i]>row[j]:
            j+=1
    return merged
def common_matrix(mat):
    common = []
    for row in mat:
        common = merge(common, row)
    return common

if __name__ == "__main__":
    print(common_matrix([[1, 2, 3, 4, 5],[2, 4, 5, 8, 10],[3, 5, 7, 9, 11],[1, 3, 5, 7, 9]]))