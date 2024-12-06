import os

# API配置
BASE_URL = "https://www.baidu.com/s"
LOGIN_URL = "https://passport.baidu.com/v2/api/?login"

# 邮件配置
EMAIL_CONFIG = {
    'smtp_server': 'smtp.qq.com',
    'smtp_port': 465,
    'username': '123455@qq.com',
    'password': os.getenv('EMAIL_PASSWORD'),
    'recipients': ['123455@sina.cn']
}

# 日志配置
LOG_CONFIG = {
    'level': 'INFO',
    'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    'filename': 'logs/test.log'
}