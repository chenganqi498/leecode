# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: 
# (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
# Write the code that will take a string and make this conversion given a number of rows:
# string convert(string text, int nRows);
# convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".

class Solution:
    # @return a string
    def convert(self, s, nRows):
        if nRows == 1: return s
        zigzag = 2*nRows-2
        rows = ['']*nRows

        for i in range(len(s)):
            if i%zigzag < nRows:
               rows[i%zigzag] += s[i]
            else:
               rows[nRows-2-(i%zigzag)%nRows] += s[i]
        out = ''
        for i in rows: out += i
        return out

if __name__ == '__main__':
   s = 'PAYPALISHIRING'
   test = Solution()
   out = test.convert(s, 3)
   print out

