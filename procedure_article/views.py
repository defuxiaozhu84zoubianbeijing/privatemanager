#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from django.template.context import RequestContext
sys.setdefaultencoding('utf-8')

from django.shortcuts import render , get_object_or_404, render_to_response
from django.http import HttpResponse , HttpResponseRedirect
from procedure_article.models import Type , Article 
from procedure_article.forms import ArticleForm 
from procedure_article import utils
import logging
from common import const
from django.db.models.aggregates import Count



# 初始化 logger
LOG = logging.getLogger(__name__)


# Create your views here.

def hello(request):
    return HttpResponse("hello world ")

def _init(request , template_name , data):
    
    # 获取文章类别
    type_set = Type.objects.filter(state=True).exclude(parentId=0)
    type_list = []
    for t in type_set:
        _dict = {}
        _dict['name'] = t.name 
        _dict['id'] = t.id 
        _dict['count'] = Article.objects.filter(state=True).filter(type=t).count()
        type_list.append(_dict)
        
    # 初始化关键字
    keyword_set = ['python', 'django', 'mysql', 'oracle', 'sqlserver', 'jquery' , 'apache' , 'bootstrap' , u'数据结构' , 'SVN' , 'Git']
    
    # 初始化文章列表
    article_new_set = Article.objects.all().order_by('-id')[:10]
    
    # 加入data中
    data['keyword_set'] = keyword_set
    data['article_new_set'] = article_new_set
    data['type_list'] = type_list
    
    return render_to_response(template_name , data , context_instance=RequestContext(request))

# 初始化显示全部
def _query(request , searchCondition):
    articles = utils.query(request, searchCondition)
        
    template_name = 'procedure_article/index.html'
    init_data = {'articles' : articles}
    return  _init(request , template_name , init_data)

# 文章增改操作
def _opreate(request , instance):
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
    template_name = 'procedure_article/article_operate.html'
    init_data = {'form' : form}
    return _init(request , template_name, init_data)

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

# #
# #   查询相关的操作 
# #
# 初始化，查询全部
def init(request):
    # 初始化文章列表
    return _query(request, None)

# 根据类别查询
def query_by_type(request , type_id=1):
    searchCondition = {
        'type' : int(type_id)
    }
    return _query(request, searchCondition)
    
# 根据关键字查询
def query_by_keyword(request, keyword='django'):
    searchCondition = {
        'keyword__icontains' : str(keyword)
    }
    return _query(request, searchCondition)

def query_by_author(request , author='wangxin'):
    searchCondition = {
        'author__icontains' : str(author)
    }
    return _query(request, searchCondition)

# 查询
def search(request):
    if request.method == 'POST':
        searchCondition = {
            'keyword__icontains' : request.POST['txt_search']
        }
        return _query(request, searchCondition)
    else :
        return _query(request, None)

# #
# #   文章增删改操作
# #
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
    template_name = 'procedure_article/article_detail.html'
    init_data = {
        'article' : article , 'article_pre' : article_pre , 'article_next' : article_next
    }
    return _init(request , template_name , init_data)

# #
# # 文章的统计操作
# # 
# 绘制统计图
def tongji(request, params):
    # 绘制统计图
    _set = Article.objects.filter(state=True)
    _options = _get_options(params , _set)
    pivchtChart = utils.draw_pivot_chart(_options)
    init_data = {'_set' : _set , '_options':_options , 'pivchtChart' : pivchtChart }
    template_name = 'procedure_article/tongji.html'
    return _init(request , template_name , init_data)
        

    





    

