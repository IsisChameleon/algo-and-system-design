import heapq
from collections import defaultdict
from datetime import datetime, timedelta
from typing import Optional, List

""" JOB SCHEDULER :

Jobs have the following characteristics:
- a priority (run asap)
- a time to run (run asap after this time)
- a deadline (run before that time)
- a list of dependencies (must run before this job)

Note. about mmultithreading https://chriskiehl.com/article/parallelism-in-one-line


"""


class Job:
    def __init__(self, job_id: int, priority: int, deadline: datetime, dependencies: Optional[List[int]] = None):
        self.job_id = job_id
        self.priority = priority
        self.deadline = deadline
        self.dependencies = dependencies or []


    """
    The __lt__ method is particularly useful when you want to use your custom objects 
    in data structures like lists, sets, or heaps, where the ability to compare objects 
    is important for sorting, searching, or prioritizing them.
    """

    def __lt__(self, other: 'Job') -> bool:
        # Compare jobs based on priority and deadline
        if self.priority == other.priority:
            return self.deadline < other.deadline
        return self.priority > other.priority

# class JobScheduler:
#     def __init__(self):
#         self.jobs = defaultdict(list)
#         self.completed_jobs = set()
#         self.running_jobs = set()
#         self.overdue_jobs = set()
#         self.failed_jobs = set()

#     def submit_job(self, job: Job):
#         for dependency in job.dependencies:
#             self.jobs[dependency].append(job)
#         if not job.dependencies:
#             heapq.heappush(self.jobs[job.job_id], job)

#     def schedule_jobs(self) -> None:
#         while self.jobs:
#             job_ids = sorted(self.jobs.keys())
#             for job_id in job_ids:
#                 if not self.jobs[job_id]:
#                     continue
#                 runnable_job = heapq.heappop(self.jobs[job_id])
#                 if all(dep in self.completed_jobs for dep in runnable_job.dependencies):
#                     self.running_jobs.add(runnable_job)
#                     self.run_job(runnable_job)

#     def run_job(self, job: Job):
#         if job.deadline < datetime.now():
#             self.overdue_jobs.add(job)
#             return
#         # Simulate job execution
#         try:
#             # Pretend the job succeeded
#             self.completed_jobs.add(job.job_id)
#         except Exception as e:
#             self.failed_jobs.add(job)

#     def monitor_jobs(self) -> None:
#         print("Completed jobs:", self.completed_jobs)
#         print("Running jobs:", self.running_jobs)
#         print("Overdue jobs:", self.overdue_jobs)
#         print("Failed jobs:", self.failed_jobs)
#         if self.priority == other.priority:
#             return self.deadline < other.deadline
#         return self.priority < other.priority

class JobScheduler:
    def __init__(self):
        self.job_queue = []  # Priority queue of jobs
        self.job_history = defaultdict(list)  # Job execution history
        self.job_dependencies = defaultdict(set)  # Job dependencies

    def submit_job(self, job):
        # Add job to the priority queue and update dependencies
        heapq.heappush(self.job_queue, job)
        for dep in job.dependencies:
            self.job_dependencies[dep].add(job.job_id)

    def schedule_jobs(self):
        # Schedule jobs that are ready to run
        while self.job_queue:
            job = self.job_queue[0]
            if all(dep_id in self.job_history for dep_id in job.dependencies):
                heapq.heappop(self.job_queue)
                self.run_job(job)
            else:
                break

    def run_job(self, job):
        # Simulate job execution
        print(f"Running job {job.job_id}")
        self.job_history[job.job_id].append(datetime.now())

        # Update dependencies for other jobs
        for dep_id in self.job_dependencies:
            if job.job_id in self.job_dependencies[dep_id]:
                self.job_dependencies[dep_id].remove(job.job_id)

    def monitor_jobs(self):
        # Check for failed or overdue jobs
        for job_id, history in self.job_history.items():
            if len(history) == 1 and (datetime.now() - history[0]) > timedelta(seconds=10):
                print(f"Job {job_id} failed to complete")
            elif len(history) > 1 and (datetime.now() - history[-1]) > timedelta(seconds=10):
                print(f"Job {job_id} is overdue")

# Example usage
scheduler = JobScheduler()

# Submit jobs
job1 = Job(1, 1, datetime.now() + timedelta(seconds=20))
job2 = Job(2, 2, datetime.now() + timedelta(seconds=15), [1])
job3 = Job(3, 3, datetime.now() + timedelta(seconds=30))

scheduler.submit_job(job1)
scheduler.submit_job(job2)
scheduler.submit_job(job3)

# Schedule and monitor jobs
while True:
    scheduler.schedule_jobs()
    scheduler.monitor_jobs()
    if not scheduler.job_queue:
        break
    time.sleep(5)  # Simulate time passing
