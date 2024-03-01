from dao.JobDao import JobDao

class JobService():

    def getJobSalaryStatisticByJobType(self):
        jobDao = JobDao()
        try:
            resultSet = jobDao.getJobSalaryStatisticByJobType()
        finally:
            jobDao.close()
        return resultSet
    
    def getJobCountStatisticByJobType(self):
        jobDao = JobDao()
        try:
            resultSet = jobDao.getJobCountStatisticByJobType()
        finally:
            jobDao.close()
        return resultSet