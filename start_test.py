import os
import sys
import logging
from datetime import datetime
from pathlib import Path
from utils.email_sender import EmailSender
from config.settings import EMAIL_CONFIG

class TestRunner:
    def __init__(self):
        self.setup_environment()
        self.timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')

    def setup_environment(self):
        """设置环境"""
        for dir_path in ['logs', 'reports/html']:
            Path(dir_path).mkdir(parents=True, exist_ok=True)

    def run_all_tests(self):
        """运行所有测试"""
        report_path = f'reports/html/report_{self.timestamp}.html'
        cmd = f'pytest --html={report_path} --self-contained-html'
        return os.system(cmd)

    def run_smoke_tests(self):
        """运行冒烟测试"""
        report_path = f'reports/html/smoke_report_{self.timestamp}.html'
        cmd = f'pytest tests/smoke/ --html={report_path} --self-contained-html'
        return os.system(cmd)

    def run_functional_tests(self):
        """运行功能测试"""
        report_path = f'reports/html/functional_report_{self.timestamp}.html'
        cmd = f'pytest tests/functional/ --html={report_path} --self-contained-html'
        return os.system(cmd)

def main():
    runner = TestRunner()
    
    # 运行所有测试
    result = runner.run_all_tests()
    
    # 或者只运行特定类型的测试
    # result = runner.run_smoke_tests()
    # result = runner.run_functional_tests()
    
    sys.exit(result)

if __name__ == "__main__":
    main()