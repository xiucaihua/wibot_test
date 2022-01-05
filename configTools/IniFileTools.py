#coding:utf-8
import configparser

"""
判断是否有指定的selection名称
@:param iniFilePath  ini文件路径
@:param selectionName selection名称
@:return result 返回一个boole类型结果
"""
def has_section(self,iniFilePath,selectionName):
    try:
        config = configparser.ConfigParser()
        path = config.read(iniFilePath)
        result=config.has_section(selectionName)
    except BaseException as msg:
        print (msg)



"""
获取到指定select下的option对应的值
@:param iniFilePath ini文件路径
@:param selectionName selection的名称
@:param optionName    option名称
@:return result       返回option对应的value值
"""
def getSelctionOfValue(iniFilePath,selectionName,optionName):
    try:
        config = configparser.ConfigParser()
        config.read(iniFilePath)
        result=config.get(selectionName,optionName)
    except BaseException as msg:
        print (msg)
    return result



"""
 增加select项
 @:param iniFilePath ini文件路径
 @:param selectionName 增加的select名称
 @:param mode 读写的模式
 """
def addSelections(iniFilePath,selectionName,mode):
    try:
        config = configparser.ConfigParser()
        path = config.read(iniFilePath)
        config.add_section(selectionName)
        config.write(open(iniFilePath, mode))
    except BaseException as msg:
        print (msg)

"""
增加指定select项下，key和value值
@:param iniFilePath ini文件路径
@:param selectionName select名称
@:param optionKey 增加的key名称
@:param optionValue 增加key对应的value名称
@:param mode 文件读写模式
"""
def addSelectOption(iniFilePath, selectionName,optionKey,optionValue,mode):
    try:
        config = configparser.ConfigParser()
        path = config.read(iniFilePath)
        config.set(selectionName,optionKey,optionValue)
        config.write(open(iniFilePath, mode))
    except BaseException as msg:
        print (msg)

"""
获取指定的select下面的所有的键值对信息
@:param iniFilePath ini文件路径
@:param selectionName select的名称
@:return list 返回key的list列表
"""
def getKey(iniFilePath,selectionName):
    try:
        config = configparser.ConfigParser()
        path = config.read(iniFilePath)
        list=config.options(selectionName)
    except BaseException as msg:
        print (msg)
    return  list

"""
获取指定的select下面的所有的键值对信息
@:param iniFilePath ini文件路径
@:param selectionName select的名称
@:return list 返回key-value列表集合
"""
def getiteams(iniFilePath,selectionName):
    try:
        config = configparser.ConfigParser()
        config.read(iniFilePath)
        list=config.items(selectionName)
    except BaseException as msg:
        print(msg)
    return list


