#coding:utf-8
import yaml

class yamlTool():
    """
    yaml文件读写操作工具类
    """

    """
    读取yaml所有的mode的所有数据
    :param YamlPath: yaml文件路径
    :param readeMode：读文件模式
    :return：content： 返回数据字典格式内容
    """
    def readAllMode(self,YamlPath,readeMode):
       file=open(YamlPath,readeMode)
       content=file.read()
       return yaml.load(content)



    """
    读取yaml指定的modeName的所有数据
    :param YamlPath: yaml文件路径
    :param readeMode：读文件模式
    :param modeName：读取的指定的块名称
    :return content： 返回数据字典格式内容
    """
    def readModeData(self,YamlPath,readeMode,modeName):
       file=open(YamlPath,readeMode)
       data = yaml.load(file.read(), Loader=yaml.FullLoader)
       return data[modeName]


    """
    读取yaml指定的modeName,key里面的数据
    :param YamlPath: yaml文件路径
    :param readeMode：读文件模式
    :param modeName：读取的指定的块名称
    :param key：读取的指定的key的内容
    :return data： 返回对应数据类型数据
    """
    def readKey(self, YamlPath, readeMode, modeName,key):
         file = open(YamlPath, readeMode)
         data=yaml.load(file.read(), Loader=yaml.FullLoader)
         return data[modeName][key]



    """
    往yaml配置文件写数据
    :param YamlPath: yaml文件路径
    :param writeMode：写入文件模式
    :param readeMode：读文件模式
    :param **kwargs：写入的yaml文件数据
    """
    def writeYaml(self,YamlPath,writeMode,readeMode,**kwargs):
        fw=open(YamlPath,writeMode)
        data=kwargs
        yaml.dump(data,fw)
        f=open(YamlPath,readeMode)
        conten=f.read()
        yaml.load(conten)

if __name__ == '__main__':
    yamltool=yamlTool()
    # keys= yamltool.readKey("D:\FramWork\configTools\yamlData.yaml","r","logger","name")
    # print("---------------",keys)

    data=yamltool.readModeData("D:\FramWork\configTools\yamlData.yaml","r","logger")
    print("---------------",data)



# def read_yaml():
#     with open("D:\FramWork\configTools\yamlData.yaml", encoding='utf-8') as f:
#         data = yaml.load(f.read(), Loader=yaml.FullLoader)
#         print(data)
#         print(data["python"]["nb1"])
#
# read_yaml()

# open方法打开直接读出来
# f = open("D:\FramWork\configTools\yamlData.yaml", 'r', encoding='utf-8')
# d = yaml.load(f.read(),Loader=yaml.FullLoader)  # 用load方法转字典
# print(d)
# print(type(d))

#正常的键值对格式的读取
# f1 = open("D:\FramWork\configTools\yamlData.yaml",'r', encoding='utf-8')
# d1 = yaml.load(f1,Loader=yaml.FullLoader)  # 使用load方法加载
# print(d1)
# print(type(d1))  # 读出类型为字典
# print(d1['user']) # 通过字典的取值来取值



# open方法打开直接读出来
# file= open("D:\FramWork\configTools\yamlData.yaml", 'r', encoding='utf-8')
# d = yaml.load(file, Loader=yaml.FullLoader)
# print(d)
# print(type(d))



# open方法打开直接读出来,以字符串方式读取出来
#f = open("D:\FramWork\configTools\yamlData.yaml", 'r', encoding='utf-8')
#cfg = f.read()
# print(type(cfg))  # 读出来是字符串
# print(cfg)

#正常以字典的方式读取出来数据
# f = open("D:\FramWork\configTools\yamlData.yaml", 'r', encoding='utf-8')
# file = f.read()
# d = yaml.load(file,Loader=yaml.FullLoader)  # 用load方法转字典
# print(d)


#正常以list中存放字典的格式读取
# f = open("D:\FramWork\configTools\yamlArry.yaml", 'r', encoding='utf-8')
# file = f.read()
# d = yaml.load(file,Loader=yaml.FullLoader)  # 用load方法转字典
# print(d)
# print(d[0])
# print(d[1])
# print(d[2])
