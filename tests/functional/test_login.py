import pytest
from utils.http_client import HttpClient
from config.settings import LOGIN_URL

@pytest.fixture
def http_client():
    return HttpClient()

@pytest.mark.functional
class TestLogin:
    """登录功能测试类"""
    
    def test_valid_login(self, http_client):
        """有效登录测试"""
        data = {
            'username': 'test_user',
            'password': 'test_pass'
        }
        response = http_client.post(LOGIN_URL, data=data)
        assert response.status_code == 200

    def test_invalid_login(self, http_client):
        """无效登录测试"""
        data = {
            'username': 'invalid_user',
            'password': 'invalid_pass'
        }
        response = http_client.post(LOGIN_URL, data=data)
        assert response.status_code == 401