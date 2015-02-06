# encoding: utf-8
from django.shortcuts import render, render_to_response, HttpResponse
from django.template import RequestContext
from django.db.models import Q, Count
from mysite.content.models import Article, IndexShowcase, CommonWidget, IndexContentBox, FooterBox
# Create your views here.

from mysite.content.forms import UrlForm
import sys

reload(sys)  # Python2.5 初始化后会删除 sys.setdefaultencoding 这个方法，我们需要重新载入
sys.setdefaultencoding('utf-8')

def index(request):
	index_show_case = IndexShowcase.objects.all()
	context = {
		'index_show_case': index_show_case,
	}
	index_content_box = IndexContentBox.objects.filter(id__in=[5, 6, 7, 8])

	for box in index_content_box:
		if box.id == 5:
			context.update({'box_1': box})
		elif box.id == 6:
			context.update({'box_2': box})
		elif box.id == 7:
			context.update({'box_3': box})
		elif box.id == 8:
			context.update({'box_4': box})

	footer_boxes = list(FooterBox.objects.all().order_by('order'))
	for box in footer_boxes:
		print 'xxx'
	context.update({'footer_boxes': footer_boxes})

	return render_to_response('content/index.html', context,
							  context_instance=RequestContext(request),
	)

def content(request, id=1):
	article = Article.objects.get(id=id)

	context = {'article': article,
			   'article_id': id,
	}

	return render_to_response('content/level_2.html', context,
							  context_instance=RequestContext(request),
	)


def level_1(request, id=1, psg=''):
	# 左侧一级菜单
	article = Article.objects.get(id=id)

	context = {'article': article,
			   'article_id': id,
	}


	# return render_to_response('html/page_man.html', context,
	# 			context_instance=RequestContext(request),
	# 				)
	return render_to_response('content/level_1.html', context,
							  context_instance=RequestContext(request),
	)


def level_2(request, id=1):
	article = Article.objects.get(id=id)
	has_subpage = False
	if article.sup_page.all():
		has_subpage = True
	context = {'article': article,
			   'article_id': id,
			   'has_subpage': has_subpage,
	}
	return render_to_response('content/level_2.html', context,
							  context_instance=RequestContext(request),
	)





def topmenu(request, id=0):
	# top菜单
	article = Article.objects.get(id=id)

	context = {'article': article,
			   'article_id': id,
			   'sub_articles': article.sup_page.all(),
	}

	return render_to_response('content/level_top.html', context,
							  context_instance=RequestContext(request))

def footer(request):
	footer_boxes = FooterBox.objects.all().order_by('order')
	context = {}
	context.update({'footer_boxes': footer_boxes})

	return render_to_response('content/footer.html', context,
							  context_instance=RequestContext(request))
