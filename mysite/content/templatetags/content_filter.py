# -*- coding: UTF-8 –*-
# from coffin import template
from django import template
from django.template import Context
from django.db.models import Q, Count

from mysite.content.models import Article
from collections import OrderedDict

from django.template import RequestContext

register = template.Library()

# @contextfunction
def render_body(article):
	# request = context['request']
	# only_one_page = ''
	body = article.body
	# return body
	t = template.loader.get_template('content/body.html')
	body_list = body.split('<!--nextpage-->')
	body_list_length = len(body_list)
	index_list = [ i for i in range(0,body_list_length)]
	context_dict = OrderedDict()
	context_dict.update({'index_list':index_list,
						 'context':body,
						 'article':article,
						 })
	if body_list_length==1:
		only_one_page = True
		body = body
		context_dict.update({'only_one_page':only_one_page,'body':body})
	else:
		for i in range(2,body_list_length):
			key = 'page'+str(i)
			value = body_list[i-1]
			context_dict.update({key:body_list[i]})

		page1 = body_list[0]
		context_dict.update({'page1':page1})
	# return Markup(render_to_response('content/body.html',context_dict))

	return t.render(Context(context_dict))

register.filter('render_body',render_body)
# register.filter_function(render_body)

@register.filter()
def render_level1_body(article):
	body = article.body

	t = template.loader.get_template('content/level_1_body.html')
	context_dict = OrderedDict()
	context_dict.update()

	sup_articles = article.sup_page.all()

	context_dict.update({'article':article,
						 'sup_articles':sup_articles,
						 })

	return t.render(Context(context_dict))


@register.filter()
def render_rightbox(article):
	t = template.loader.get_template('content/rightbox.html')
	context_dict = OrderedDict()
	conmon_widgets = article.common_widget.all()

	context_dict.update({'widget_set':article.widget_set.all(),
						 'conmon_widgets':conmon_widgets,})

	return t.render(Context(context_dict))


@register.filter()
def render_left_menu(article):
	t = template.loader.get_template('content/left_menu.html')
	context_dict = OrderedDict()
	condition = Q(type_first=article.type_first) & Q(menu_level=1)
	articles = Article.objects.filter(condition).all() # 实际要加入过滤条件
	context_dict.update({'articles':articles,
						 'article_id':article.id,
						 })

	return t.render(Context(context_dict))

@register.filter()
def render_left_submenu(article):
	t = template.loader.get_template('content/left_submenu.html')
	context_dict = OrderedDict()
	articles = article.sup_page.all()
	context_dict.update({'articles':articles})

	return t.render(Context(context_dict))

@register.filter()
def get_suppage_in_topmenu_body(article):
	t = template.loader.get_template('content/subpage_in_topmenu_body.html')
	context_dict = OrderedDict()
	articles =article.sup_page.all() # 实际要加入过滤条件

	context_dict.update({'articles':articles,
						 'article_id':article.id,
						 })

	return t.render(Context(context_dict))

@register.filter()
def render_level2_body_with_subpage(article):
	t = template.loader.get_template('content/subpage_in_leve2_body.html')
	context_dict = OrderedDict()
	articles =list(article.sup_page.all().order_by()) # 实际要加入过滤条件
	articles_tuple_list = zip(*2*[iter(articles)])
	if len(articles)%2==1:
		articles_tuple_list.append((articles[-1],None))
	context_dict.update({'articles':articles,
						 'article_id':article.id,
						 'article':article,
						 'articles_tuple_list':articles_tuple_list,
						 })

	return t.render(Context(context_dict))

@register.filter()
def get_class(article):
	articles = article.sup_page.all()
	if len(articles)>0:
		return "class=iner"
	else:
		return ""

@register.filter()
def has_subpage(article):
	articles = article.sup_page.all()
	if len(articles)>0:
		return True
	else:
		return False
@register.filter()
def get_subpage(article):
	articles = article.sup_page.all()
	return articles
