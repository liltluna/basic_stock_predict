from flask import request, session, render_template, Blueprint
from service.JobService import JobService
import json


jobController = Blueprint('jobController', __name__)

jobService = JobService()

# return data in the json format
@jobController.route('/salarybytype', methods = ['get', 'post'])
def getSalaryStatisticByJobType():
    resultSet = jobService.getJobSalaryStatisticByJobType()
    return json.dumps(resultSet, ensure_ascii=False)

@jobController.route('/countbytype', methods = ['get', 'post'])
def getCountStatisticByJobType():
    resultSet = jobService.getJobCountStatisticByJobType()
    return json.dumps(resultSet, ensure_ascii=False)