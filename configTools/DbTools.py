#coding:utf-8
import MySQLdb

class DbTools:

    """
    数据库连接
    @:param host           数据库地址
    @:param username       数据库用户
    @:param password       密码
    @:param dbName         连接数据库名
    @:param port           数据库连接端口
    """
    def getConnet(self,host,username,password,dbName,port=3305):
        try:
            conn = MySQLdb.connect(host, username, password, dbName,port)
            print ("连接数据库成功!")
        except BaseException as msg:
            raise BaseException("数据库连接异常")
        return conn




    """
     获取所一行数据信息
     @:param sql 执行SQL语句
     @:return result 查询结果
     """
    def getOneData(self,host,username,password,dbName,sql,port=3305):
        try:
            curs =self.getConnet(host,username,password,dbName).cursor()

           # sql = "SELECT * from test"
            '''数据操作'''
            curs.execute(sql)  # 执行数据库

            '''获取一条数据'''
            print (curs.fetchone())
        except BaseException as msg:
            print (msg)
        #return self.result

    # """
    #  获取多个数据信息
    #  @:param sql 执行SQL语句
    #  @:return result 查询结果
    #  """
    # def getManyData(self,sql):
    #     try:
    #         self.curs = self.__init__()
    #         self.curs.execute(sql)
    #         result=self.curs.fetchmany()
    #     except BaseException as msg:
    #         print msg
    #     return result
    #
    #
    # """
    # 关闭connct连接对象
    # """
    # def closeConct(self):
    #     try:
    #         self.conn.close()
    #     except BaseException as msg:
    #         raise BaseException ("关闭conn连接对象失败!")
    #
    #
    # """
    # 关闭curs连接对象
    # """
    # def closeCurs(self):
    #     try:
    #         self.curs.close()
    #     except BaseException as msg:
    #         raise BaseException ("关闭curs连接对象失败!")

if __name__ == '__main__':
    db=DbTools()
    db.getOneData('127.0.0.1', 'root', '123456', 'test',"SELECT * from test")

