class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        if A == []: return
        record = {}
        for i in A:
           if i in record: record.pop(i)
           else: record[i] = 1
        return record.keys()[0]
