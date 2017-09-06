# -*- coding:utf-8 -*-
import logging
from django.shortcuts import render
from django.conf import settings
from django.core.paginator import Paginator,InvalidPage, EmptyPage,PageNotAnInteger
from models import *
from django.db.models import Count



logger = logging.getLogger('bokeli.views')

# Create your views here.
def global_setting(request):
    SITE_NAME = settings.SITE_NAME
    SITE_DESC = settings.SITE_DESC
    WEIBO_SINA = settings.WEIBO_SINA
    WEIBO_TENCEUT = settings.WEIBO_TENCEUT
    PRO_RSS = settings.PRO_RSS
    PRO_EMAI = settings.PRO_EMAIL
    # 分类信息获取（导航数据）
    category_list = Catagory.objects.all()[:7]
    #文章归档的数据
    archive_list = Article.objects.distinct_date()
    # 广告数据（个人完成）
    #标签云数据
    #友情链接数据
    #文章排行榜数据
    #评论排行（评论的多少来排行）
    comment_count_list = Comment.objects.values('article').annotate(comment_count=Count('article')).order_by('-comment_count')
    article_comment_list =  [Article.objects.get(pk=comment['article'])for comment in comment_count_list]
    return locals()

def index(request):
    try:
        # 最新文章数据
        article_list = Article.objects.all()
        article_list = getpage(request, article_list)

        # 文章归档
        # 1先要获取文章中的日期时间

        for a in Article.objects.distinct_date():
            pass
    except Exception as e:
        print e
        logger.error(e)
    return render(request, 'index.html', locals())


def archive(request):
    try:
        # 先获取客户端提交的信息
        year = request.GET.get('year', None)
        month = request.GET.get('month' , None)
        # 先获取客户端提交的信息
        article_list = Article.objects.filter(date_publish__icontains=year+'-'+month)
        article_list = getpage(request, article_list)
    except Exception as e:
        logger.error(e)
    return render(request,'archive.html', locals())






#分页代码

def getpage(request,article_list):
    paginator = Paginator(article_list, 4)
    try:
        page = int(request.GET.get('page', 1))  # (当前页的数据，是用request获取数据没有传入数据返回1）
        article_list = paginator.page(page)  # 这里把当前页的数据传入进去，就会返回当前页的数据
    except(EmptyPage, InvalidPage, PageNotAnInteger):
        article_list = paginator.page(2)
    return article_list


# 文章详情

def article(request):
    try:
    #获取文章id
        article = Article.objects.get(pk=id)
    except Article.DoesNotExist:
        return render(request, 'failure.html', {'reason': '没有找到对应的文章'})




def comment_post(request):
    try:
        pass
    except Exception as e:
        logger.error(e)
    return render(request,'comment_post.html', locals())




def do_login(request):
    try:
        pass
    except Exception as e:
        logger.error(e)
    return  render(request,'login.html',locals())



def do_reg(request):
    try:
        pass
    except Exception as e:
        logger.error(e)
    return  render(request,'reg.html',locals())



def category(request):
    try:
        pass
    except Exception as e:
        logger.error(e)
    return  render(request,'reg.html',locals())

