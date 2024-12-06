import pytest
from utils.http_client import HttpClient
from config.settings import BASE_URL

@pytest.fixture
def http_client():
    return HttpClient()

def test_search_valid_query(http_client):
    """测试有效搜索查询"""
    params = {'wd': 'Python'}
    response = http_client.get(BASE_URL, params=params)
    assert response.status_code == 200, "Expected status code 200"
    assert 'Python' in response.url, "Expected 'Python' in URL"

def test_search_empty_query(http_client):
    """测试空搜索查询"""
    params = {'wd': ''}
    response = http_client.get(BASE_URL, params=params)
    assert response.status_code == 200, "Expected status code 200"
    assert 'www.baidu.com' in response.url, "Expected redirect to Baidu homepage"

def test_search_special_characters(http_client):
    """测试特殊字符搜索"""
    params = {'wd': '!@#$%^&*()'}
    response = http_client.get(BASE_URL, params=params)
    assert response.status_code == 200, "Expected status code 200"

def test_search_long_query(http_client):
    """测试长查询搜索"""
    long_query = 'a' * 100
    params = {'wd': long_query}
    response = http_client.get(BASE_URL, params=params)
    assert response.status_code == 200, "Expected status code 200"

def test_search_chinese_query(http_client):
    """测试中文搜索"""
    params = {'wd': '自动化测试'}
    response = http_client.get(BASE_URL, params=params)
    assert response.status_code == 200, "Expected status code 200"