import os.path
import yaml
from typing import Any
from injector import inject,singleton

@inject
@singleton
class ProviderFactory:
    """服务提供商工厂类"""
    provider_tool_map:dict[str,Any] = None

    def __init__(self):
        """构造函数，初始伦对应的provider_tool_map"""
        self._get_provider_tool_map()

    def _get_provider_tool_map(self):
        """项目初始化的时候获取报务提供商，工具的映射关系并填充provider_tool_map"""
        # 1. 检测provider_tool_map量否为空
        if self.provider_tool_map:
            return

        # 2. 获取当前文件/类所在的文件夹路径
        current_path = os.path.abspath(__file__)
        provider_path = os.path.dirname(current_path)
        provider_yaml_path = os.path.join(provider_path, 'providers.yaml')

        # 3. 读取providers.yaml的数据
        with open(provider_yaml_path,encoding='utf-8') as f:
            providers_yaml_data = yaml.safe_load(f)


        # 4. 循环遍历providers.yaml的数据
        for idx,provider_data in enumerate(providers_yaml_data):




