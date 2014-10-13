class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        if A == []: return
        record = {}
        for i in A:
            if i not in record: record[i] = 1
            elif record[i] < 2: record[i] += 1
            else: record.pop(i)
        return record.keys()[0]
