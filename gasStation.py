# There are N gas stations along a circular route, 
# where the amount of gas at station i is gas[i].

# You have a car with an unlimited gas tank 
# and it costs cost[i] of gas to travel from station i to its next station (i+1). 
# You begin the journey with an empty tank at one of the gas stations.

# Return the starting gas station's index if you can travel around the circuit once, 
# otherwise return -1.

# Note:
# The solution is guaranteed to be unique.

class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        N = len(gas)
        for start in range(N): 
            count, res = 0, 0
            for i in range(start, start + N):
                curr = res + gas[i/N] 
                res = curr - cost[i/N]
                if res < 0: break 
                count += 1
            if count == N: return start
        return -1 


