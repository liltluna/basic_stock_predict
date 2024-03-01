from dao.BaseDao import BaseDao

# DAO：database access object
class StockDao(BaseDao):

    # basic stock info
    def createStock(self, params=[]):
        sql = "insert into stock_basic (ts_code, symbol, name, area, industry, list_date) " \
              "values (%s, %s, %s, %s, %s, %s)"  # %s是占位符
        result = self.execute(sql ,params)
        self.commit()
        return result
 
    # count stock numbers
    def getStockNumbers(self):
        sql = '''SELECT COUNT(*) FROM stock_basic'''
        result = self.execute(sql=sql)
        resultSet = self.fetchall()
        return resultSet
    
    # count data numbers
    def getDataNumbers(self):
        sql = '''SELECT COUNT(*) FROM index_daily'''
        result = self.execute(sql=sql)
        resultSet = self.fetchall()
        return resultSet

    # get all data of PingAn Bank
    def getAllDataOfPABank(self):
        sql = '''select trade_date, `open`, high, low, `close` from index_daily where ts_code='000001.SZ' '''
        result = self.execute(sql=sql)
        resultSet = self.fetchall()
        return resultSet
    
    def getSampleStockInfo(self):
        # get the first ten piece info as sample
        sql = 'select * from stock_basic limit 10'
        result = self.execute(sql=sql)
        resultSet = self.fetchall()
        return resultSet
    
    def getStockWithDetails(self):
        sql = '''SELECT * FROM stock_basic WHERE ts_code IN (SELECT DISTINCT ts_code FROM index_daily); '''
        result = self.execute(sql=sql)
        resultSet = self.fetchall()
        return resultSet
    
    def getSpecificData(self, symbol):
        sql = '''select trade_date, `open`, high, low, `close` from index_daily where ts_code='''
        sql += "'" + symbol + ".SZ'"
        result = self.execute(sql=sql)
        resultSet = self.fetchall()
        return resultSet
    
    def getPredictedData(self, symbol):
        sql = '''select close, predictions from valid_predict where symbol='''
        sql += "'" + symbol + "'"
        result = self.execute(sql=sql)
        resultSet = self.fetchall()
        return resultSet

    def getSpecificDateData(self, symbol):
        sql = '''select trade_date, close from index_daily where ts_code='''
        sql += "'" + symbol + ".SZ'"
        result = self.execute(sql=sql)
        resultSet = self.fetchall()
        return resultSet

if __name__ == '__main__':
    # change path before run
    stockDao = StockDao()
    resultSet = stockDao.getStockNumbers()
    print(resultSet)
    stockDao.close()
