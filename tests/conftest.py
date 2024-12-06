import pytest
from datetime import datetime

def pytest_html_report_title(report):
    report.title = "自动化测试报告"

def pytest_configure(config):
        # 检查是否有 _metadata 属性
        if hasattr(config, '_metadata'):
            config._metadata['项目名称'] = '自动化测试项目'
            config._metadata['测试时间'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            config._metadata['冒烟测试'] = '包含'
            config._metadata['其他测试'] = '包含'
            # config._metadata['项目名称'] = '自动化测试项目'
            # config._metadata['测试时间'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        else:
            # 如果没有 _metadata，可以考虑其他方式记录信息
            print("项目名称: 自动化测试项目")
            print("测试时间:", datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

def pytest_html_results_summary(prefix, summary, postfix):
    prefix.extend(["""
        <p>测试环境: 测试环境</p>
        <p>测试人员: 测试人员</p>
    """])

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    report.description = str(item.function.__doc__)