#!/usr/bin/env python
# -*- coding: utf-8 -*- 

## Copyright 2011, IOActive, Inc. All rights reserved.
##
## AndBug is free software: you can redistribute it and/or modify it under 
## the terms of version 3 of the GNU Lesser General Public License as 
## published by the Free Software Foundation.
##
## AndBug is distributed in the hope that it will be useful, but WITHOUT ANY
## WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS 
## FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for 
## more details.
##
## You should have received a copy of the GNU Lesser General Public License
## along with AndBug.  If not, see <http://www.gnu.org/licenses/>.
   
   
#文件功能：实现日志记录的一些类功能：
#对外提供一下函数接口：
#def error(tag, meta, data = None)      输出错误信息
#def info(tag, meta, data = None)		输出普通信息
#def read_log(path=None, file=None)		读取日志信息

   
import os, sys, time
from cStringIO import StringIO

def blocks(seq, sz):
    ofs = 0
    lim = len(seq)
    while ofs < lim:
        yield seq[ofs:ofs+sz]  #关键是yield的用法，现在理解的还不是很深入
        ofs += sz
		
#函数功能：
#注释：censor 审查，检查
#将传入的字符编程可打印字符，对于传入的不可打印字符，用“.”表示
def censor(seq):
    for ch in seq:
        if ch < '!': 
            yield '.'
        elif ch > '~':
            yield '.'
        else:
            yield ch


#函数功能：以十六制形式输出数据【猜测】
def format_hex(data, indent="", width=16, out=None):
    if out == None:
        out = StringIO()  #StringIO经常被用来作为字符串的缓存，应为StringIO有个好处，他的有些接口和文件操作是一致的，也就是说用同样的代码，可以同时当成文件操作或者StringIO操作
        strout = True
    else:
        strout = False

    indent += "%08x:  "
    ofs = 0
    for block in blocks(data, width): #将一个字符串按照指定的长度分成多个字符串段
        out.write(indent % ofs)
        out.write(' '.join(map(lambda x: x.encode('hex'), block)))
        if len(block) < width:
            out.write( '   ' * (width - len(block)) )
        out.write('  ')
        out.write(''.join(censor(block)))
        out.write(os.linesep)
        ofs += len(block)

    if strout:
        return out.getvalue()

def parse_hex(dump, out=None):
    if out == None:
        out = StringIO()
        strout = True
    else:
        strout = False

    for row in dump.splitlines():
        row = row.strip().split('  ')  #strip函数用于去掉字符串中开始和结束的字符
        block = row[1].strip().split(' ')
        block = ''.join(map(lambda x: chr(int(x, 16)), block))
        out.write(block)

    if strout:
        return out.getvalue()

class LogEvent(object):
    def __init__(self, time, tag, meta, data):
        self.time = time
        self.tag = tag
        self.meta = meta
        self.data = data or ''
    
    def __str__(self):
        return "%s %s %s\n%s" % (
            self.tag, self.time, self.meta, 
            format_hex(self.data, indent="    ")
        )

class LogWriter(object):
    def __init__(self, file=sys.stdout):
        self.file = file
        
    def writeEvent(self, evt):
        self.file.write(str(evt))

class LogReader(object):
    def __init__(self, file=sys.stdin):
        self.file = file
        self.last = None
    
    def readLine(self):
        if self.last is None:
            line = self.file.readline().rstrip()  #rstrip()用来在字符串末尾删除某个字符
        else:
            line = self.last
            self.last = None
        return line

    def pushLine(self, line):
        self.last = line

    def readEvent(self):
        line = self.readLine()
        if not line: return None
        if line[0] == ' ':
            return self.readEvent() # Again..
         
        tag, time, meta = line.split(' ', 3)
        time = int(time)
        data = []

        while True:
            line = self.readLine()
            if line.startswith( '    ' ):
                data.append(line)
            else:
                self.pushLine(line)
                break
                
        if data:
            data = parse_hex('\n'.join(data))
        else:
            data = ''

        return LogEvent(time, tag, meta, data)

cur_path = os.getcwd()
err_file = open(cur_path + os.path.sep + "err.log", "a")
infor_file = open(cur_path + os.path.sep + "infor.log", "a")
debug_file = open(cur_path + os.path.sep + "debug.log", "a")
stderr = LogWriter(err_file)
stdout = LogWriter(infor_file)
stdebug = LogWriter(debug_file)

def error(tag, meta, data = None):
    now = int(time.time())
    stderr.writeEvent(LogEvent(now, tag, meta, data))

def info(tag, meta, data = None):
    now = int(time.time())
    stdout.writeEvent(LogEvent(now, tag, meta, data))

def debug(tag, meta, data=None):
    
    now = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    now +="(%f)" %(time.time())
    #now = int(time.time())
    stdout.writeEvent(LogEvent(now, tag, meta, data))
    

def read_log(path=None, file=None):
    if path is None:
        if file is None:
            reader = LogReader(sys.stdin)
        else:
            reader = LogReader(file)
    return reader


def debug_infor (infor, filepath="/home/anbc/workspace/log/debug_infor.txt"):
    '''
        add by anbc for debug the program
    '''
    file_object = open(filepath, 'a')
    file_object.write(infor+"\r\n")
    file_object.close( )


def main():
    print 'start'    

    debug("test", "infor")
   
    
    print 'end' 

    

if __name__ == '__main__':
    main()     