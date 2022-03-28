import os
import yaml


# 创建类
class YamlReader:

    # 初始化，判断文件是否存在
    def __init__(self, yamlfile):
        if os.path.exists(yamlfile):
            self.yamlfile = yamlfile
        else:
            raise FileNotFoundError("文件不存在")
        self._data_all = None

    # yaml读取多个文件
    def data_all(self):
        # 第一次调用需要读取yaml文档；非第一次调用，直接返回之前保存的数据
        if not self._data_all:
            with open(self.yamlfile, "r", encoding="utf-8") as result:
                self._data_all = list(yaml.safe_load_all(result))
                # self._data_all = yaml.safe_load(result)    读取单个文件
        return self._data_all
