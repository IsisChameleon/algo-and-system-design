def twoNumberSum(array, targetSum):
    # Write your code here.
    sa = sorted(array)
    start = 0
    end = len(array)-1
    results = findTwoNumberSum(sa, start, end, targetSum)
    
    return results

# O(nlog(n)) time , O(1) space
def findTwoNumberSum(sa, start, end, targetSum):
    current_sum = sa[start]+sa[end]
    print(f'sorted {sa}, start {start} end {end}, sum {current_sum}')
    if current_sum == targetSum:
        return [sa[start], sa[end]]
    if current_sum > targetSum and (end-start>1):
        end-=1                                                              
        return findTwoNumberSum(sa, start, end, targetSum)
    if current_sum < targetSum and (end-start>1):
        start+=1
        return findTwoNumberSum(sa, start, end, targetSum)
    return []