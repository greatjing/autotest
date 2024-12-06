import smtplib
import logging
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from config.settings import EMAIL_CONFIG

class EmailSender:
    def __init__(self, smtp_server, smtp_port, username, password):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_email(self, subject, body, to_emails, attachment_path=None):
        try:
            logging.info(f"准备发送邮件到: {to_emails}")
            
            msg = MIMEMultipart()
            msg['From'] = self.username
            msg['To'] = ', '.join(to_emails)
            msg['Subject'] = subject

            # 添加HTML正文
            msg.attach(MIMEText(body, 'html'))

            # 添加附件
            if attachment_path:
                logging.info(f"添加附件: {attachment_path}")
                try:
                    with open(attachment_path, 'rb') as f:
                        part = MIMEApplication(f.read(), Name='report.html')
                    part['Content-Disposition'] = f'attachment; filename="report.html"'
                    msg.attach(part)
                    logging.info("附件添加成功")
                except Exception as e:
                    logging.error(f"添加附件失败: {str(e)}")
                    raise

            # 连接SMTP服务器并发送
            logging.info(f"连接SMTP服务器: {self.smtp_server}:{self.smtp_port}")
            with smtplib.SMTP_SSL(self.smtp_server, self.smtp_port) as server:
                logging.info("SMTP连接成功，尝试登录...")
                server.login(self.username, self.password)
                logging.info("登录成功，发送邮件...")
                server.sendmail(self.username, to_emails, msg.as_string())
                logging.info("邮件发送成功")

        except Exception as e:
            logging.error(f"发送邮件失败: {str(e)}")
            raise