# two sum
'''
# this worked but too slow
class Solution:
    def twoSum(self, array, target):
        for i in range(len(array)):
            for j in range(i, len(array)):
                if array[i] + array[j] == target: 
                    print 'index1=', i+1, 'index2=', j+1
'''    
class Solution:
    def twoSum(self, num, target):
        dict = {}
        for i in range(len(num)):          
            if dict.get(target-num[i]) == None:
                dict[num[i]] = i 
            else:
                return (dict[target-num[i]]+1, i+1)
                            
                    
if __name__ == '__main__':
    lt = [1,3,2,4,4,5,6,7,8,0]
    out = Solution()
    print out.twoSum(lt, 9)
    
    