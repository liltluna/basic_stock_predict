from dao.BaseDao import BaseDao

# 职位数据管理数据库操作类   DAO：database access object
class JobDao(BaseDao):

    # job info
    def createJob(self, params=[]):
        sql = "insert into t_jobs (jobname,jobsalary, jobCompany, jobaddress,jobDetail, jobType,jobLowSalary, jobHighSalary, jobMeanSalary, jobCity) " \
              "values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"  # %s是占位符
        result = self.execute(sql ,params)
        self.commit()
        return result

    # job salary
    def getJobSalaryStatisticByJobType(self):
        sql = 'select avg(jobmeansalary) as meansalary, jobtype from t_jobs GROUP BY jobType'
        result = self.execute(sql=sql)
        resultSet = self.fetchall()
        return resultSet
    
    # job numbers
    def getJobCountStatisticByJobType(self):
        sql = 'select count(jobtype) as nums, jobtype from t_jobs group by jobtype'
        result = self.execute(sql=sql)
        resultSet = self.fetchall()
        return resultSet
    
if __name__ == '__main__':
    jobDao = JobDao()
    resultSet = jobDao.getJobSalaryStatisticByJobType()
    print(resultSet)
    jobDao.close()
