from typing import List, Tuple
import bisect

def find_max_profit(jobs: List[Tuple[int, int, int]]) -> int: # start time, end time, profit
    # Sort jobs by end time
    jobs.sort(key=lambda x: x[1])
    n = len(jobs)
    
    # dp[i] will store the maximum profit by considering the first i jobs (0-indexed)
    dp = [0] * n
    
    # Store just the end times to use with bisect
    end_times = [job[1] for job in jobs]

    dp[0] = jobs[0][2]
    
    for i in range(1, n):
        start, end, profit = jobs[i]
        # Find the last non-overlapping job using binary search
        job_finishing_before_i = bisect.bisect_right(end_times, start) - 1
        
        # dp[i] is the maximum of not taking this job (meaning we get dp[i-1]) or taking this job (profit + job finishing before i profit)
        if job_finishing_before_i != -1:
            dp[i] = max(dp[i - 1], dp[job_finishing_before_i] + profit)
        else:
            dp[i] = max(dp[i - 1], profit)
    
    return dp[-1]

def max_profit_for_multiple_test_cases(test_cases: List[List[Tuple[int, int, int]]]) -> List[int]:
    results = []
    for jobs in test_cases:
        results.append(find_max_profit(jobs))
    return results

# Example usage
if __name__ == "__main__":
    T = int(input())  # Number of test cases
    test_cases = []
    
    for _ in range(T):
        N = int(input())  # Number of jobs
        jobs = []
        for _ in range(N):
            start, end, profit = map(int, input().split())
            jobs.append((start, end, profit))
        test_cases.append(jobs)
    
    results = max_profit_for_multiple_test_cases(test_cases)
    for result in results:
        print(result)
