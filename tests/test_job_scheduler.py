import unittest
from datetime import datetime, timedelta
from coding_pattern.job_scheduler import Job, JobScheduler

class TestJobScheduler(unittest.TestCase):
    def test_submit_job(self):
        scheduler = JobScheduler()
        job = Job(1, 1, datetime.now() + timedelta(hours=2), dependencies=[])
        scheduler.submit_job(job)
        self.assertEqual(len(scheduler.jobs[1]), 1)

    def test_schedule_jobs(self):
        scheduler = JobScheduler()
        job1 = Job(1, 1, datetime.now() + timedelta(hours=2), dependencies=[])
        job2 = Job(2, 2, datetime.now() + timedelta(hours=1), dependencies=[1])
        scheduler.submit_job(job1)
        scheduler.submit_job(job2)
        scheduler.schedule_jobs()
        self.assertEqual(len(scheduler.running_jobs), 1)
        self.assertEqual(len(scheduler.completed_jobs), 1)

    def test_run_job(self):
        scheduler = JobScheduler()
        job = Job(1, 1, datetime.now() + timedelta(hours=2), dependencies=[])
        scheduler.run_job(job)
        self.assertEqual(len(scheduler.completed_jobs), 1)

    def test_monitor_jobs(self):
        scheduler = JobScheduler()
        job1 = Job(1, 1, datetime.now() + timedelta(hours=2), dependencies=[])
        job2 = Job(2, 2, datetime.now() - timedelta(hours=1), dependencies=[])
        scheduler.submit_job(job1)
        scheduler.submit_job(job2)
        scheduler.schedule_jobs()
        scheduler.monitor_jobs()
        self.assertIn(1, scheduler.completed_jobs)
        self.assertIn(2, scheduler.overdue_jobs)

if __name__ == '__main__':
    unittest.main()
