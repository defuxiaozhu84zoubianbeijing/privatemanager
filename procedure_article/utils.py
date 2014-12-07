#!/usr/bin/python
# -*- coding: utf-8 -*-
from procedure_article.models import Type , Article
from xml.etree import ElementTree
from chartit import PivotDataPool, PivotChart 
from django.db.models.aggregates import  Count
from chartit.chartdata import DataPool
from chartit.charts import Chart

# 查询
def query(request , params):
    
    if isinstance(params, str):
        articles = Article.objects.filter(state=True).filter(keyword__icontains=params)
    elif isinstance(params, int) :
        instance = Type.objects.get(pk=params)
        articles = Article.objects.filter(state=True).filter(type=instance)
        # 简单的补救
    else :
        articles = Article.objects.filter(state=True)
    return articles
    
# 解析xml文件
def read_xml(path):
    choices = [] 
    root = ElementTree.fromstring(open(path).read()) 
    nodes = root.getiterator("choice")
    for node in nodes :
        choices.append(node.text)
    return choices

# 功能说明：获取上一篇、下一篇 , id:对应博客id
def get_neighbour(_obj , _list):
    dic = {}
    pre = None
    _next = None 
    
    _list = list(_list)
    if _list:
        id_index = _list.index(_obj)  # 当前id的索引

        if len(_list) > 1:
            if id_index != 0 and id_index != len(_list) - 1:  # 如果不是第一篇或最后一篇
                pre = _list[id_index - 1]
                _next = _list[id_index + 1]
            else:
                if id_index == 0:  # 第一篇
                    _next = _list[id_index + 1]
                if id_index == len(_list) - 1:  # 最后一篇
                    pre = _list[id_index - 1]
        elif len(_list) == 1:
            pre, _next = None, None
        dic = {'pre': pre, '_next': _next}
    return dic


    
# 绘制pivot统计图表
def draw_pivot_chart(options):
    '''
             传入参数：
             1._type :chart的类型 是柱状图（column），线状图（line)饼状图（pie)
             2._set :数据源集合
             3._categories : 集合分类的标准，集合按照_categories分类，是model的field（字段)
             3._terms_name : terms的名称
             4._terms_val :terms的值，支持Sum/Avg/Counnt等函数
             5._chart_text : chart 标题显示的文字
             6._x_axis_text :chart x轴显示的文字
             
            返回值 ：
            1.返回 pivchtChart
    '''
    ds = PivotDataPool(
        series=[{
            'options': {
               'source': options['_set'],
               'categories': options['_categories']
            },
            'terms': {
                options['_terms_name']: options['_terms_val']
                }}
             ])
    
    
    pivcht = PivotChart(
        datasource=ds,
        series_options=[{
            'options':{
                'type': options['_type'],
                'stacking': True},
                'terms':options['_terms_name_list']
            }],
        chart_options={
            'title': {
                'text': options['_chart_text']},
            'xAxis': {
                'title': {
                    'text': options['_x_axis_text']
                }
             }
        }
    )

    return pivcht

'''
 ds = DataPool(
       series=
        [{'options': {
            'source': Article.objects.all()},
          'terms': [
            'publishdate', 'id']}
         ])

    pivcht = Chart(
            datasource=ds,
            series_options=
              [{'options':{
                  'type': type,
                  'stacking': False},
                'terms':{
                  'publishdate': [
                     '编号']
                  }}],
            chart_options=
              {'title': {
                   'text': '根据发布日期统计文章数量'},
               'xAxis': {
                    'title': {
                       'text': '发布日期'}},
               'yAxis': {
                    'title': {
                       'text': '文章编号'}},
               })
    
'''
        
    
    
    
    
