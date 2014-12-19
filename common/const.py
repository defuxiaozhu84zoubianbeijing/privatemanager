#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


'''
存储privatemanager网站中使用的常量
'''
# procedure_article 
# 权限常量
PERMESSION_ADD_ARTICLE = 'procedure_article.add_article'  # 添加文章权限
PERMESSION_CHANGE_ARTICLE = 'procedure_article.change_article'  # 修改文章权限
PERMESSION_DELETE_ARTICLE = 'procedure_article.delete_article'  # 删除文章权限
PERMESSION_DELETE_COMMENT = 'procedure_article.delete_comment'  # 删除评论权限

# accounts
ACTIVE_CODE_SUBJECT = u'私人管家网站激活码'  # 获取网站激活码邮件标题
PWD_GET_SUBJECT = u'私人管家网站找回密码'  # 找回密码
ORIGINAL_PWD = '1234567890'  # 网站原始登录密码



