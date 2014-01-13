#!/usr/bin/env python
# -*- coding: utf-8 -*- 



import subprocess, threading, os, os.path
import time
import re
import hashlib
from pyDes import *

from errors import *
import log


















class ShellException( Exception ):
    def __init__( self, command, output, status ):
        self.command = command
        self.output = output
        self.status = status

def printout( prefix, data ):
    data = data.rstrip()
    if not data: return ''
    print prefix + data.replace( '\n', '\n' + prefix )

#创建一个进程，去执行一个指定的command
def sh( command, no_echo=True, no_fail=False, no_wait=False ):
    if not no_echo: 
        printout( '>>> ', repr( command ) )

    process = subprocess.Popen( 
        command,
        stdout = subprocess.PIPE,
        stderr = subprocess.STDOUT,
        stdin = None,
        shell = True if isinstance( command, str ) else False
    )
    
    if no_wait: return process

    output, _ = process.communicate( )
    status = process.returncode
    print "status=" + str(status)
    if status: 
        if not no_echo: printout( '!!! ', output )
        if not no_fail: raise ShellException( command, output, status )
    else:
        if not no_echo: printout( '::: ', output )

    return output

def ShellIOOld( command):
    '''
    临时增加以便解决多次输入的问题
    '''
    print "begin"
    process = subprocess.Popen( 
        command,
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE,
        stdin = subprocess.PIPE,
        shell = True if isinstance( command, str ) else False
    )
    
    print "end"
    return process


def ShellIO(command, timeout=20):
    '''
    临时增加以便解决多次输入的问题
    '''
    print "begin"
    process = subprocess.Popen( 
        command,
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE,
        stdin = subprocess.PIPE,
        shell = True if isinstance( command, str ) else False
    )
    
    
    #output, _ = process.communicate()
    #print output
   
    time.sleep(timeout)
    
    if timeout!=0:
        output, _ = process.communicate("exit \n")
    else:
        output, _ = process.communicate()
        
    status = process.returncode
    print output
    print "status=" + str(status)

    return output

def FileMd5(filePath):
    '''
    函数功能：计算目标文件的md5
    '''
    file = None;  
    bRet = False;  
    strMd5 = "";  
      
    try:  
        file = open(filePath, "rb");  
        md5 = hashlib.md5();  
        strRead = "";  
          
        while True:  
            strRead = file.read(8096);  
            if not strRead:  
                break;  
            md5.update(strRead);  
                #read file finish  
        bRet = True;  
        strMd5 = md5.hexdigest();  
            
    except:  
        bRet = False; 
        
    finally:  
        if file:  
            file.close()  
  
    return [bRet, strMd5];  


def Encrypt(sData):
    k = des("TBLAS1.0", CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)
    d = k.encrypt(sData)
    return d.encode('hex')

def Decrypt(sData):
    sData = sData.decode('hex')
    k = des("TBLAS1.0", CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)
    return k.decrypt(sData)



def main():
        
        
    ShellIOTest("andbug monitor -p com.colorme.game.yujianvhaiqq  /home/anbc/workspace/diting/sample/3aff2a49c40db0ee3bb44a868d4ddc83/3aff2a49c40db0ee3bb44a868d4ddc83.log")
    
    
    print "game over"



if __name__ == '__main__':
    main()