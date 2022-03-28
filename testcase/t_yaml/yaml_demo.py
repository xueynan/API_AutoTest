"""
    yaml使用
"""
import yaml
# 1、创建yaml的文件:data.yaml
# 2、读取单个文件
# with open("./data.yaml", "r", encoding="utf-8") as file:
#     result = yaml.safe_load(file)
# # 3、输出文件
#     print(result)


# 读取多个文件
# 1、编辑或修改data.yaml
# 2、yaml读取方法，all
# with open("./data.yaml", "r", encoding="utf-8") as file:
#     result = yaml.safe_load_all(file)
# # 3、循环打印
#     for r in result:
#         print(r)


from utils.yaml_utils import YamlReader

result = YamlReader("./data.yaml").data_all()
print(result)
