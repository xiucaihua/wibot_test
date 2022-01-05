#coding:utf-8
import os

"""
读取所有的文件
@:param  filePath 读写文件的路径
@:param  mode 文件的读写模式
@:return content返回所有的文件内容
"""
def readAll(filePath,mode):
    try:
        file = open(filePath, mode)
        content = file.read()
        file.close()
    except BaseException as msg:
        print (msg)
    finally:
        file.close()
    return content

"""
读取一行文件内容
@:param  filePath 读写文件的路径
@:param  mode 文件的读写模式
@:return content返回所有的文件内容
"""
def readLine(filePath,mode):
    try:
        file = open(filePath, mode)
        content = file.readline()
    except BaseException as msg:
        print (msg)
    finally:
        file.close()
    return content



"""
写入文件内容
@:param  filePath 读写文件的路径
@:param  mode 文件的读写模式
@param  content写入文件的内容
@:raise BaseException 文件写入异常
"""
def write(filePath,mode,content):
    try:
        with open(filePath, mode) as f:
            f.write(content)
    except BaseException as msg:
        raise  BaseException(content,"写入文件失败！")
    finally:
        f.close()


""""
多行写入文件内容
@:param  filePath 读写文件的路径
@:param  mode 文件的读写模式
@param  content写入文件的内容
"""
def writeLine(filePath,mode,content):
    try:
        with open(filePath, mode) as f:
            f.writelines(content)
    except BaseException as msg:
        raise  BaseException(content,"写入文件失败！")


"""
读取分隔符数据
@:param  filePath 读写文件的路径
@:param  mode 文件的读写模式
@:return value 返回第一个数据
@:return value2 返回第二个数据
"""
def readLinesOfNum(filePath, mode):
    try:
        file=open(filePath, mode)
        lines=file.readline()
        for line in lines:
            value=lines.split(",")[0]
            value2=lines.split(",")[1]
    except BaseException as msg:
        print (msg)
    finally:
        file.close()
    return value,value2
