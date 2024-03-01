import pymysql
import json
import os

class BaseDao():
    '''
    数据库访问基类
    '''
    def __init__(self, config="mysql.json"):
        self.__config = json.load(open(config, mode="r", encoding="utf-8"))  # 读取mysql.json配置文件，转为python对象
        self.__conn = None
        self.__cursor = None

        pass

    def getConnection(self):
        if self.__conn != None:
            return self.__conn
        self.__conn = pymysql.connect(**self.__config)   # **{"host":"127.0.0.1", "user":"root", "password":"root", "database":"db_jobsdata", "port":3306, "charset":"utf8"}
        return self.__conn

    def execute(self, sql , params=[], ret="dict"):
        result = 0
        try:
            self.__conn = self.getConnection()
            if ret == "dict":
                self.__cursor = self.__conn.cursor(pymysql.cursors.DictCursor)  # 返回字典数据
            else:
                self.__cursor = self.__conn.cursor()                            # 返回元组数据
            result = self.__cursor.execute(sql, params)
        except pymysql.DatabaseError as e:
            print(e)
        return result

    def fetchone(self):
        if self.__cursor:
            return self.__cursor.fetchone()

    def fetchall(self):
        if self.__cursor:
            return self.__cursor.fetchall()

    def close(self):
        if self.__cursor:
            self.__cursor.close()

        if self.__conn:
            self.__conn.close()

    def commit(self):
        if self.__conn:
            self.__conn.commit()

    def rollback(self):
        if self.__conn:
            self.__conn.rollback()

if __name__ == '__main__':
    bD = BaseDao()
