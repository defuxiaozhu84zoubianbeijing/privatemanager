#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.core.mail.message import EmailMultiAlternatives, BadHeaderError
from django.core import mail



# 检查邮箱地址
def check_email(_email):
    # 暂时没想好 如何检测邮箱
    return _email

# 发送邮件
def _send_mail(request , options):
    '''
    options 参数：
        1. text_content : 邮件的文本内容
        2. html_content : 邮件的html内容，如果邮件为html文件
        3. to_mail : 邮件发送至 xxx邮箱的地址
        4. subject : 邮件标题内容
        5. from_email : 邮件发出邮箱的地址
    dict 返回值：
        1. flag : 邮件发送成功与否 , True 代表成功  . False : 代表失败
    
    '''
    _dict = None
    try:
        subject = options['subject']
        from_email = options['from_email']
        text_content = options['text_content']
        html_content = options['html_content']
        msg = EmailMultiAlternatives(subject, text_content, from_email, [options['to_mail']])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        _dict = {'flag' : True }
    except BadHeaderError as er:
        print er
        _dict = {'flag' : False }
        
    return  _dict 

# 创建邮件列表
def get_notification_email(_messages_list=[]):
    _emails = [] 
    for m in _messages_list :
        _email = mail.EmailMessage(m['subject'] , m['html_content'] , m['from_email'], m['to_mail'])
        _email.content_subtype = 'html'
        _emails.append(_email)
    return _emails

# 群发邮件
def send_multiple_email(options):
    try :
        connection = mail.get_connection()  # 使用默认邮件链接(connection)
        _emails = get_notification_email(options)
        connection.send_messages(_emails)
        return  True 
    except Exception as er :
        print er 
        return False 

    





