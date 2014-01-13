#!/usr/bin/env python
#coding=utf-8

# This database.py support MySQL only

import os,time
import PySQLPool
#from base import *

import config
import util



########################################################################################################################
###

# 封装了数据库的操作，在整个系统里面，它才是唯一真正跟数据库打交道的类
class DBOperation():
    def __init__(self, dbServerName):
        '''
        函数功能：
        参数：sDbServerName 选择操作数据库的放
        '''
        if config.g_databaseInfor[dbServerName]["watch_dog"]==False:
            #首次运行
            config.g_databaseInfor[dbServerName]["password"] = self.DecryptPassword(config.g_databaseInfor[dbServerName]["password"])
            config.g_databaseInfor[dbServerName]["watch_dog"] = True

        connection = PySQLPool.getNewConnection(username=config.g_databaseInfor[dbServerName]["user"], 
                                                password=config.g_databaseInfor[dbServerName]["password"], 
                                                host=config.g_databaseInfor[dbServerName]["addr"], 
                                                port =config.g_databaseInfor[dbServerName]["port"], 
                                                db = config.g_databaseInfor[dbServerName]["db_name"], 
                                                charset='utf8')
        self.pDBConn = connection
        

        
    def DecryptPassword(self, decPassword):
        return util.Decrypt(decPassword)

    def Debug(self, sMsg):
        try:
            print sMsg
        except Exception,e:
            print 'Exception: ',e

    def Query(self, sSql, args=None):
        self.Debug(sSql)
        query = PySQLPool.getNewQuery(self.pDBConn)
        query.query(sSql, args)
        return query.record

    def ExcuteSql(self, sSql, args=None):
        self.Debug(sSql)
        insert = PySQLPool.getNewQuery(self.pDBConn)
        insert.query(sSql, args)
        return insert.lastInsertID

    def ExcuteSqlBat(self, sSqls, args=None):
        inserts = PySQLPool.getNewQuery(self.pDBConn)
        inserts.query(sSqls, args)
        return inserts.lastInsertID

    def Update(self, sSql, args=None):
        self.Debug(sSql)
        update = PySQLPool.getNewQuery(self.pDBConn)
        update.query(sSql, args)
        return update.affectedRows
    
    def Commit(self):
        return

def TestPerf():
    for i in range(1000):
        oDb = DBOperation()
        sSql = 'select * from Objects'
        oDb.ExcuteSql(sSql)


def TestConnect(sAddr, nPort, sUser, sPasswd):
    try:
        testConn = PySQLPool.getNewConnection(username=sUser, password=sPasswd, host=sAddr, port=nPort, db='mysql', charset='utf8')
        query = PySQLPool.getNewQuery(testConn)
        query.query(r'select * from user')

        return True, '成功'
    except Exception,e:
        print e
        return False,e




def CreateTable():
    try:
        f = open(os.path.join('.', 'conf', 'init.sql'))
        lines = f.readlines()
        f.close()
    except Exception, e:
        print e
        return

    try:
        conn = DBOperation('tbsoc')
        for sql in lines:
            try:
                conn.ExcuteSql(sql)
            except Exception,e:
                print e

    except Exception, e:
        print e





if "__main__" == __name__:
#    print get_2db_instance().__str__
#    print get_2db_instance().__str__
#    print get_2db_instance().__str__
#    begin = GetNow3()
#    TestPerf()
#    print GetNow3() - begin
    
    CreateTable()
