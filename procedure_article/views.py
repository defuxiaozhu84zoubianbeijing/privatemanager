#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse , HttpResponseRedirect
from procedure_article.models import Type , Article , Comment
from procedure_article.forms import ArticleForm , CommentForm
from procedure_article import utils
from datetime import datetime
import logging
from common import const
from django.db.models.aggregates import Count

# 初始化 logger
LOG = logging.getLogger(__name__)

# 从xml中读取autocomplete的source数据
'''
def init_search(request):
    path = 'E:\\test.xml'
    return HttpResponse(utils.read_xml(path))
'''

# Create your views here.

def hello(request):
    return HttpResponse("hello world ")

# 初始化显示全部
def _query(request , instance):
    
    type_level2_set = []
    type_level1_set = Type.objects.filter(state=True).filter(parentId=0)
    for t in type_level1_set : 
        type_level2_set.append(Type.objects.filter(state=True).filter(parentId=t.id))
    type_level2_set.reverse()
    
    articles = utils.query(request, instance)
    return render(request , 'procedure_article/index.html' , locals()) 

# 初始化，查询全部
def init(request):
    # 初始化文章列表
    return _query(request, None)

# 根据类别查询
def query_by_type(request , type_id=1):
    return _query(request, int(type_id))
    
# 根据关键字查询
def query_by_keyword(request, keyword='django'):
    return _query(request, str(keyword))

# 查询
def search(request):
    if request.method == 'POST':
        keyword = request.POST['txt_search']
        if keyword is None or keyword == '':
            keyword = 'django'
        return _query(request, str(keyword))
    else :
        return _query(request, None)

# 操作
def _opreate(request , instance):
        
    # 初始化 nav
    type_level2_set = []
    type_level1_set = Type.objects.filter(state=True).filter(parentId=0)
    for t in type_level1_set : 
        type_level2_set.append(Type.objects.filter(state=True).filter(parentId=t.id))
    type_level2_set.reverse()
    # 初始化复选框
    # path = 'E:\\test.xml'
    # choices = utils.read_xml(path)
    
    form = None 
    if request.method == 'POST' :
        keyword_str = ''
        for key in request.POST.getlist('keyword'):
            keyword_str += key + ' '
            
        form = ArticleForm(request.POST , request.FILES , instance=instance)
        if form.is_valid():
            article = form.save(commit=False)
            article.keyword = keyword_str
            article.save()
            LOG.debug(request.user.__unicode__() + u': 操作' + article.title + u'成功')
            return HttpResponseRedirect('/procedure_article/init/')
    else :
        form = ArticleForm(instance=instance) 
    return render(request , 'procedure_article/article_operate.html' , locals())

# 添加文章
def add(request):
    if request.user.has_perm(const.PERMESSION_ADD_ARTICLE) :
        LOG.debug(request.user.__unicode__() + u': 添加文章 ')
        return _opreate(request , None)
    else :
        return HttpResponseRedirect('/procedure_article/init/')
# 修改文章
def update(request , article_id):
    if request.user.has_perm(const.PERMESSION_CHANGE_ARTICLE) :
        article = Article.objects.get(pk=article_id)
        LOG.debug(request.user.__unicode__() + u': 修改文章')
        return _opreate(request , article)
    else :
        return HttpResponseRedirect('/procedure_article/init/')

# 显示文章详情 , 发布评论 ,评论时验证用户登录
def detail(request, article_id=1):
        
    # 初始化 nav
    type_level2_set = []
    type_level1_set = Type.objects.filter(state=True).filter(parentId=0)
    for t in type_level1_set : 
        type_level2_set.append(Type.objects.filter(state=True).filter(parentId=t.id))
    type_level2_set.reverse()
        
    # 文章
    article = article_pre = article_next = None 
    if article_id is not None :
        try :
            article = get_object_or_404(Article , pk=article_id)
            article_list = Article.objects.filter(state=True).order_by('publishdate')
            dict = utils.get_neighbour(article , article_list)
            article_pre = dict['pre']
            article_next = dict['_next'] 
        except Exception as er :
            LOG.error('error : ' + str(er))
            print er
            pass 
    comments = article.comment_set.filter(state=True).order_by('publishdate')
    
    return _op_comment(request , article , article_pre, article_next , comments , type_level2_set , type_level1_set)
        
    
# 发布评论
def _op_comment(request , article , article_pre, article_next , comments , type_level2_set , type_level1_set):
    
    # 初始化
    comments = comments
    type_level2_set = type_level2_set
    type_level1_set = type_level1_set
    # 评论
    form = None 
    if request.method == 'POST':
        form = CommentForm(request.POST , request.FILES)
        author = request.POST['author']
        if form.is_valid():
            # 判断用户是否登录 
            if request.user.is_authenticated():
                comment = form.save(commit=False)
                comment.author = author
                comment.article = article
                comment.publishdate = datetime.now()
                comment.save() 
                LOG.debug(request.user.__unicode__() + u': 发表评论 成功')
                return HttpResponseRedirect('/procedure_article/articles/' + str(article.id) + '/detail/') 
            else :
                # 用户没登陆，则跳转到登陆页面
                LOG.debug(request.user.__unicode__() + u': 没有登录，不能发表评论')
                return HttpResponseRedirect('/accounts/login/')
    else:
        form = CommentForm()
    return render(request , 'procedure_article/article_detail.html' , locals())

# 删除评论
def del_comment(request , article_id , comment_id):
    if request.user.has_perm(const.PERMESSION_DELETE_COMMENT):
        comment = get_object_or_404(Comment , pk=comment_id)
        if comment is not None :
            comment.delete()
            LOG.debug(request.user.__unicode__() + u' : 删除评论 成功')
    return HttpResponseRedirect('/procedure_article/articles/' + article_id + '/detail/')


# 发表评论
'''
def publish(request):
    # 保存评论  
    form = None 
    message = ''
    if request.method == 'POST':
        form = CommentForm(request.POST , request.FILES)
        author = request.POST['author']
        article_id = request.POST['article_id']
        article = Article.objects.get(pk=article_id)
        if form.is_valid():
            comment = form.save(commit=False);
            comment.author = author
            comment.article = article
            comment.save()   
    else:
        form = CommentForm()
    return render(request , 'procedure_article/article_detail.html' , locals())
'''
# 获取绘制统计图需要的option书
# _type='column' , _set , _categories , _terms_name , _terms_val , _chart_text , _x_axis_text
def _get_options(params , _set):
    options = {}
    if params == 'column' :
        options = {
           '_type' : 'column' ,
           '_set' : _set,
           '_categories' : 'type__name',
           '_terms_name' : u'发布数量',
           '_terms_name_list' : [u'发布数量'],
           '_terms_val'  : Count('id'),
           '_chart_text' : u'根据文章类别统计发布数量' ,
           '_x_axis_text' : u'类别' ,
       }
    elif params == 'line' :
        options = {
           '_type' : 'line' ,
           '_set' : _set,
           '_categories' : 'publishdate',
           '_terms_name' : u'发布数量',
           '_terms_name_list' : [u'发布数量'],
           '_terms_val'  : Count('id'),
           '_chart_text' : u'根据发布日期统计发布数量' ,
           '_x_axis_text' : u'发布日期' ,
       }
    return options 
        

# 绘制统计图
def tongji(request, params):
    # 初始化 nav
    type_level2_set = []
    type_level1_set = Type.objects.filter(state=True).filter(parentId=0)
    for t in type_level1_set : 
        type_level2_set.append(Type.objects.filter(state=True).filter(parentId=t.id))
    type_level2_set.reverse()
    # 绘制统计图
    _set = Article.objects.filter(state=True)
    _options = _get_options(params , _set)
    pivchtChart = utils.draw_pivot_chart(_options)
    return render(request , 'procedure_article/tongji.html' , locals())


    

