#! /usr/bin/env python
#coding=utf-8

import time
import threading
import json
#from base import *
import database
import hashlib
import pickle




# 获得数据库实例
def get_db(dbServerName):
    return database.DBOperation(dbServerName)

def iquery(dbServerName, sSql, args=None):
    try:
        oDb = get_db(dbServerName)
        rcds = oDb.Query(sSql, args)
        if len(rcds) > 0:
            return rcds

        return []
    except Exception,e:
        print 'Exception in data.iquery: ', e
        return  []

# 
def iqueryx(dbServerName, sSql, args=None, prefix='', timeout=3600):
 

    try:
        oDb = get_db(dbServerName)
        rcds = oDb.Query(sSql, args)
        
        return rcds

    except Exception,e:
        print 'Exception in data.iquery: ', e
        return  []

# 同步执行SQL语句
def iexecute(dbServerName, sSql, args=None):
    try:
        oDb = get_db(dbServerName)
        lastInsertID = oDb.ExcuteSql(sSql, args)
        return lastInsertID
    except Exception,e:
        print 'Exception in data.iexecute: ', e
        return  -1

# 同步执行更新SQL语句
def iupdate(dbServerName, sSql, args=None):
    oDb = get_db(dbServerName)
    affectedRows = oDb.Update(sSql, args)
    return affectedRows
    
# 同步执行删除SQL语句
def idelete(dbServerName, sSql, args=None):
    oDb = get_db(dbServerName)
    affectedRows = oDb.Update(sSql, args)
    return affectedRows
    
# 异步执行SQL语句，需要事先启动CDataToDB的线程
def asyn_iexecute(dbServerName, sSql):
    #return get_2db_instance().PushData(sSql)
    pass

# 获得记录数
def get_count2(sql):
    try:
        rcds = iquery(sql)
        if rcds:
            return rcds[0].values()[0]
        else:
            return -1
    except Exception, e:
        print 'get count error:',e
        return -1

def get_rcds2(sql):
    try:
        rcds = iquery(sql)
        return rcds
    except Exception, e:
        print 'get records error:',e
        return []


# 获得记录数
# conn为数据库实例句柄，sql为获取数量的sql语句
def get_count(conn, sql):
    try:
        rcds = conn.Query(sql)
        return rcds[0].values()[0]
    except Exception, e:
        print 'get count error:',e
        return -1



def get_rcds(conn, sql):
    try:
        rcds = conn.Query(sql)
        return rcds
    except Exception, e:
        print 'get records error:',e
        return []

# 将数据库记录封装成前端ext.grid.panel控件需要的json格式
def get_json(cnt, rcds):
    if not rcds:
        rcds = ()
        
    rsts= {}
    rsts['total'] = cnt
    rsts['items'] = list(rcds)
    
    return json.dumps(rsts)

def dump_2_json(rstdict):
    return json.dumps(rstdict)

def get_format_data(dt):
    return json.dumps(dt)

    
# 暂时没有处理
def checkQueryName(queryName):
    if queryName:
        return True

    return False
        
# 暂时没有处理
def checkQueryValue(queryValue):
    if queryValue:
        index = queryValue.find("'")
        if index == -1: return True

    return False


def main():
    print 'aaa'    
    #sSql = "SELECT violation_manager AS Leader FROM %s WHERE id=%%s" % ('dlp_Alert',)
    #INSERT INTO Persons (LastName, Address) VALUES ('Wilson', 'Champs-Elysees')
    '''
    id\ task_file_md5
    '''
    #sSql = "INSERT INTO test (task_file_md5) VALUES (%s)"
    #print sSql
    #iexecute(sSql, ['33333'])
    
    
    sql = "Show tables"
    sql 
    record = iexecute("loc_temp_db", sql, [])
    
    record = iexecute("remote_soc_db_test", sql, [])
        
    print 'bbb'
    

if __name__ == '__main__':
    main()


