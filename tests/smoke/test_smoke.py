import pytest
from utils.http_client import HttpClient
from config.settings import BASE_URL, LOGIN_URL

@pytest.fixture
def http_client():
    return HttpClient()

@pytest.mark.smoke
class TestSmoke:
    """冒烟测试类"""

    @pytest.mark.smoke
    def test_homepage_access(self, http_client):
        """首页访问测试"""
        response = http_client.get(BASE_URL)
        assert response.status_code == 200

    @pytest.mark.smoke
    def test_login_page_access(self, http_client):
        """登录页面访问测试"""
        response = http_client.get(LOGIN_URL)
        assert response.status_code == 200