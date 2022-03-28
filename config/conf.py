import os
from utils.yaml_utils import YamlReader

# 获取当前文件的绝对路径
current = os.path.abspath(__file__)  # E:\python\API_AutoTest\config\conf.py
# 获取当前项目的绝对路径   # E:\python\API_AutoTest\config
BASE_DIR = os.path.dirname(os.path.dirname(current))

# 定义config目录的路径
_config_path = BASE_DIR + os.sep + "conf"

# 定义config.yaml文件的路径
_config_file = _config_path + os.sep + "conf.yaml"


def get_config_path():
    return _config_path


def get_config_file():
    return _config_file


# 2、读取配置文件
class ConfigYaml:
    def __init__(self):
        self.config = YamlReader(get_config_file()).data_all()
    #     定义方法获取需要信息

    def get_conf_url(self):
        return self.config["BASE"]["test"]["url"]


if __name__ == "__main__":
    # conf_read = ConfigYaml()
    print(ConfigYaml().get_conf_url())
