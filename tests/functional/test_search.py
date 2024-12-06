import pytest
from utils.http_client import HttpClient
from config.settings import BASE_URL

@pytest.fixture
def http_client():
    return HttpClient()

@pytest.mark.functional
class TestSearch:
    """搜索功能测试类"""
    
    def test_basic_search(self, http_client):
        """基本搜索功能测试"""
        params = {'wd': 'Python'}
        response = http_client.get(BASE_URL, params=params)
        assert response.status_code == 200
        assert 'Python' in response.url

    def test_empty_search(self, http_client):
        """空搜索测试"""
        params = {'wd': ''}
        response = http_client.get(BASE_URL, params=params)
        assert response.status_code == 200