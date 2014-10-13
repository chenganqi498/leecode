# Given an absolute path for a file (Unix-style), simplify it.

# For example,
# path = "/home/", => "/home"
# path = "/a/./b/../../c/", => "/c"

class Solution:
      # @param path, a string
      # @return a string
      def simplifyPath(self, path):
          if path == '': return ''
          sep = path.split('/')
          newpath = []
          for i in range(len(sep)):
              if sep[i] == '..' and newpath != []:
                 newpath.pop()
              elif sep[i] != '' and sep[i] != '.' and sep[i] != '..': 
                 newpath.append(sep[i])
              if newpath == [] and i == len(sep)-1: 
                 newpath.append('')
          out = ''
          for i in newpath: out += '/'+i
          return out

if __name__ == '__main__':
   path = "/home/"
   test = Solution()
   out = test.simplifyPath(path)
   print out          




