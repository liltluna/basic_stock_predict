from dao.StockDao import StockDao

class StockService():

    def getSampleStockInfo(self):
        stockDao = StockDao()
        try:
            resultSet = stockDao.getSampleStockInfo()
        finally:
            stockDao.close()
        return resultSet
    
    def getAllDataOfPABank(self):
        stockDao = StockDao()
        try:
            resultSet = stockDao.getAllDataOfPABank()
        finally:
            stockDao.close()
        formatted_result = [
            [
                f"{data['trade_date'][:4]}/{data['trade_date'][4:6]}/{data['trade_date'][6:]}",
                data['open'],
                data['close'],
                data['low'],
                data['high'],
            ]
            for data in resultSet
        ]
        formatted_result.reverse()
        return formatted_result

    def getStockNumbers(self):
        stockDao = StockDao()
        try:
            resultSet = stockDao.getStockNumbers()
        finally:
            stockDao.close()
        return resultSet
    
    def getDataNumbers(self):
        stockDao = StockDao()
        try:
            resultSet = stockDao.getDataNumbers()
        finally:
            stockDao.close()
        return resultSet
    
    def getStockWithDetails(self):
        stockDao = StockDao()
        try:
            resultSet = stockDao.getStockWithDetails()
        finally:
            stockDao.close()
        return resultSet
    
    def getSpecificData(self, symbol):
        stockDao = StockDao()
        try:
            resultSet = stockDao.getSpecificData(symbol)
        finally:
            stockDao.close()
        formatted_result = [
            [
                f"{data['trade_date'][:4]}/{data['trade_date'][4:6]}/{data['trade_date'][6:]}",
                data['open'],
                data['close'],
                data['low'],
                data['high'],
            ]
            for data in resultSet
        ]
        formatted_result.reverse()
        return formatted_result
    
    def getPredictedData(self, symbol):
        stockDao = StockDao()
        try:
            pResultSet = stockDao.getPredictedData(symbol)
            dResultSet = stockDao.getSpecificDateData(symbol)
        finally:
            stockDao.close()
        formatted_result_p = [[item['close'], item['predictions']] for item in pResultSet]
        formatted_result_d = [[item['trade_date'], item['close']] for item in dResultSet]
        formatted_result = {
            'pre' : formatted_result_p,
            'trade_date' : formatted_result_d
        }
        # formatted_result.reverse()
        return formatted_result