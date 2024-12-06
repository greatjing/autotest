import requests
import logging
from typing import Optional, Dict, Any

class HttpClient:
    """HTTP客户端工具类"""
    
    def __init__(self):
        self.session = requests.Session()
        self.logger = logging.getLogger(__name__)

    def get(self, url: str, params: Optional[Dict[str, Any]] = None) -> requests.Response:
        """发送GET请求"""
        try:
            self.logger.info(f"发送GET请求: {url}, params: {params}")
            response = self.session.get(url, params=params)
            self.logger.info(f"响应状态码: {response.status_code}")
            return response
        except Exception as e:
            self.logger.error(f"GET请求失败: {str(e)}")
            raise

    def post(self, url: str, data: Optional[Dict[str, Any]] = None) -> requests.Response:
        """发送POST请求"""
        try:
            self.logger.info(f"发送POST请求: {url}, data: {data}")
            response = self.session.post(url, data=data)
            self.logger.info(f"响应状态码: {response.status_code}")
            return response
        except Exception as e:
            self.logger.error(f"POST请求失败: {str(e)}")
            raise