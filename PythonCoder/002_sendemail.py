#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
构造一个邮件对象就是一个Messag对象，如果构造一个MIMEText对象，就表示一个文本邮件对象，如果构造一个MIMEImage对象，就表示一个作为附件的图片，
要把多个对象组合起来，就用MIMEMultipart对象，而MIMEBase可以表示任何对象。它们的继承关系如下：
Message
+- MIMEBase
   +- MIMEMultipart
   +- MIMENonMultipart
      +- MIMEMessage
      +- MIMEText
      +- MIMEImage
'''

__author__ = 'GQ'

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.header import Header
from email import encoders

#服务器，端口，登录名，密码
MAIL_HOST = "smtp.163.com"
MAIL_PORT = 25
MAIL_USERNAME = "fxx@163.com"
MAIL_PASSWD = "xx"
#收件人，发件人，主题，内容
to_list = ["4xx@qq.com", "guxx@126.com"]
sender = "fxxx@163.com"
subject = "Python send mail"
send_text = """
     自动发送邮件，无需回复。\n
     www.pyhton.org
"""
class MailClient(object):

    def __init__(self):
        pass

    def __enter__(self):
        self.server = smtplib.SMTP()
        self.server.connect(MAIL_HOST, MAIL_PORT)
        self.server.login(MAIL_USERNAME, MAIL_PASSWD)
        return self

    # 因为邮件主题、显示发件人、收件人等信息并不是通过SMTP协议发给MTA，而是包含在发给MTA的文本中的，所以，我们必须把From、To和Subject添加到MIMEText中.
    def _send_text(self, sender, to_list, subject, send_text, text_type):
        msg = MIMEText(send_text.encode("utf-8"), _subtype=text_type, _charset='utf-8')
        msg['Subject'] = subject
        me = "<" + sender + ">"
        msg['From'] = me
        msg['To'] = ";".join(to_list)   # 接收的是字符串而不是list
        self.server.sendmail(sender, to_list, msg.as_string())

    # 发送附件
    def _Multi_send_text(self, sender, to_list, subject, send_text):
        msg = MIMEMultipart()  # 邮件对象，MIMEMultipart('alternative')
        msg['Subject'] = Header(subject)
        me = "<" + sender + ">"
        msg['From'] = me
        msg['To'] = ";".join(to_list)   # 接收的是字符串而不是list
        # 邮件正文是MIMEText:
        msg.attach(MIMEText(send_text.encode("utf-8"),  _charset='utf-8'))
        '''
        图片内嵌邮件正文中的发送方式：（只需修改下面的一行代码即可实现）
        在HTML中通过引用src="cid:0"就可以把附件作为图片嵌入了。如果有多个图片，给它们依次编号，然后引用不同的cid:x即可。
        '''
        # msg.attach(MIMEText('<html><body><h1>'+send_text.encode("utf-8") +'</h1>' + '<p><img src="cid:0"></p>' + '</body></html>', 'html', 'utf-8'))

        # 添加附件就是加上一个MIMEBase，从本地读取一个图片:
        with open('刺客聂隐娘.jpg', 'rb') as f:
            # 设置附件的MIME和文件名，这里是png类型:
            # mime = MIMEBase('image', 'png', filename='pic.png')
            mime = MIMEBase('application', 'octet-stream')  # 'octet-stream': binary data
            # 加上必要的头信息:
            mime.add_header('Content-Disposition', 'attachment', filename='pic.png')  # 附件名称
            mime.add_header('Content-ID', '<0>')
            mime.add_header('X-Attachment-Id', '0')
            # 把附件的内容读进来:
            mime.set_payload(f.read())
            # 用Base64编码:
            encoders.encode_base64(mime)
            # 添加到MIMEMultipart:
            msg.attach(mime)
        self.server.sendmail(sender, to_list, msg.as_string())

    # 文本形式的文件
    def send_plain_text(self, sender, to_list, subject, send_text):
        self._send_text(sender, to_list, subject, send_text, 'plain')

    # html形式的邮件
    def send_html(self, sender, to_list, subject, send_text):
        self._send_text(sender, to_list, subject, send_text, 'html')

    # 附件形式的邮件
    def send_attach(self, sender, to_list, subject, send_text):
        self._Multi_send_text(sender, to_list, subject, send_text)

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.server.close()
        return False

if __name__ == "__main__":
    with MailClient() as client:
        # client.send_plain_text(sender, to_list, subject, send_text)
        # client.send_html(sender, to_list, subject, send_text)
        client.send_attach(sender, to_list, subject, send_text)