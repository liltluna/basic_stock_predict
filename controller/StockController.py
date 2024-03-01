from flask import request, session, render_template, Blueprint
from service.StockService import StockService
import json
# from keras.models import load_model
# import pandas as pd
# import numpy as np
# from sklearn.preprocessing import MinMaxScaler


# loaded_model = load_model('./models/lstm_model.h5')


stockController = Blueprint('stockController', __name__)

stockService = StockService()

# return data in the json format
@stockController.route('/sample', methods = ['get', 'post'])
def getSampleStockInfo():
    resultSet = stockService.getSampleStockInfo()
    return json.dumps(resultSet, ensure_ascii=False)

# get all data
@stockController.route('/pingandata', methods = ['get', 'post'])
def getAllDataOfPABank():
    resultSet = stockService.getAllDataOfPABank()
    return json.dumps(resultSet, ensure_ascii=False)

# get the number of stock types
@stockController.route('/stocknums', methods = ['get', 'post'])
def getStockNumbers():
    resultSet = stockService.getStockNumbers()
    return json.dumps(resultSet, ensure_ascii=False)

# get the number of data
@stockController.route('/datanums', methods = ['get', 'post'])
def getDataNumbers():
    resultSet = stockService.getDataNumbers()
    return json.dumps(resultSet, ensure_ascii=False)

# get stock with details
@stockController.route('/stockdetails', methods = ['get', 'post'])
def getStockWithDetails():
    resultSet = stockService.getStockWithDetails()
    return json.dumps(resultSet, ensure_ascii=False)

# get specific data
@stockController.route('/specificdata', methods = ['get', 'post'])
def getSpecificData():
    if request.method == 'POST':
        # 获取前端传递的symbol参数
        symbol = request.form.get('symbol')
        resultSet = stockService.getSpecificData(symbol)
        return json.dumps(resultSet, ensure_ascii=False)

# get prediction
@stockController.route('/predicteddata', methods = ['get', 'post'])
def getPredictedData():
    if request.method == 'POST':
        # 获取前端传递的symbol参数
        symbol = request.form.get('symbol')
        resultSet = stockService.getPredictedData(symbol)
        return json.dumps(resultSet, ensure_ascii=False)
        
        # dataset = stockService.getAllDataOfPABank()
        # # dataset.reverse()
        # # 取第一列和第二列
        # selected_data = [[row[0], row[1]] for row in dataset]
        # # 创建DataFrame
        # df = pd.DataFrame(selected_data, columns=['trade_date', 'close'])
        # df = df[['trade_date', 'close']]
        # df['trade_date'] = pd.to_datetime(df['trade_date'])
        # df.set_index('trade_date', inplace=True)
        # # Create a new dataframe with only the 'Close column 
        # data = df.filter(['close'])
        # # Convert the dataframe to a numpy array
        # datavalues = data.values
        # # Get the number of rows to train the model on
        # scaler = MinMaxScaler(feature_range=(0,1))
        # scaled_data = scaler.fit_transform(datavalues)
        # training_data_len = int(np.ceil( len(dataset) * .95 ))
        # # Create the testing data set
        # # Create a new array containing scaled values from index 1543 to 2002 
        # test_data = scaled_data[training_data_len - 60: , :]
        # # Create the data sets x_test and y_test
        # x_test = []
        # y_test = datavalues[training_data_len:, :]
        # for i in range(60, len(test_data)):
        #     x_test.append(test_data[i-60:i, 0])
        # # Convert the data to a numpy array
        # x_test = np.array(x_test)
        # # Reshape the data
        # x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1 ))

        # # Get the models predicted price values 
        # predictions = loaded_model.predict(x_test)
        # predictions = scaler.inverse_transform(predictions)

        # valid = data[training_data_len:]
        # valid['predictions'] = predictions
        # valid_reset = valid.reset_index()

        # # 将日期格式调整为"YYYY/MM/DD"
        # valid_reset['trade_date'] = valid_reset['trade_date'].dt.strftime('%Y/%m/%d')

        # # 提取所需的列并转换为列表的列表
        # resultSet= valid_reset[['trade_date', 'predictions']].values.tolist()
        # return json.dumps(resultSet, ensure_ascii=False)   