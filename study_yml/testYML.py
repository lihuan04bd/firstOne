import unittest
from ddt import ddt,file_data
@ddt
class TestYaml(unittest.TestCase):
    #读取yaml 文件中的数据，并传入测试用例
    # 专门用于处理字典格式的参数的传参方式
    @file_data("data.yaml")
    def test_yaml_1(self, **kwargs):
        print(kwargs)

if __name__ == '__main__':
    unittest.main()