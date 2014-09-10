# Given an array of words and a length L, 
# format the text such that each line has exactly L characters and is fully (left and right) justified.

# You should pack your words in a greedy approach; 
# that is, pack as many words as you can in each line. 
# Pad extra spaces ' ' when necessary so that each line has exactly L characters.

# Extra spaces between words should be distributed as evenly as possible. 
# If the number of spaces on a line do not divide evenly between words, 
# the empty slots on the left will be assigned more spaces than the slots on the right.

# For the last line of text, 
# it should be left justified and no extra space is inserted between words.

# For example,
# words: ["This", "is", "an", "example", "of", "text", "justification."]
# L: 16.

# Return the formatted lines as:
# [
#   "This    is    an",
#   "example  of text",
#   "justification.  "
# ]
# Note: Each word is guaranteed not to exceed L in length

class Solution:
    # @param words, a list of strings
    # @param L, an integer
    # @return a list of strings
    def fullJustify(self, words, L):
        if words == []: return
        i = 0
        out = []
        while i < len(words):
           count, l = 0, 0
           line = ''
           while i+count < len(words) and l+len(words[i+count]) <= L:
              l += len(words[i+count]) + 1 # 1 comes from ' '
              count += 1
          
           l -= 1 # drop the last ' '
           fill = L-l
           if count == 1 or i+count == len(words): # only one word or last line
              for add in range(count-1):
                 line += words[i+add]+' '
              line += words[i+count-1] + ' '*fill
           else: 
              even = fill / (count-1)
              res = fill % (count-1)
              for add in range(count-1):
                 space = even+2 if res>0 else even+1
                 line += words[i+add]+' '*(space)
                 res -= 1
              line += words[i+count-1]
           out.append(line)
           i += count
        return out

if __name__ == '__main__':
   w1 = ["This", "is", "an", "example", "of", "text", "justification."]
   w2 = ["What","must","be","shall","be."]
   w3 = ["Don't","go","around","saying","the","world","owes","you","a","living;","the","world","owes","you","nothing;","it","was","here","first."]
   test = Solution()
   out = test.fullJustify(w3, 15)
   print out


