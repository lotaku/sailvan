# -*- coding: UTF-8 –*-
# from coffin import template
from django import template
from django.template import Context
from django.db.models import Q, Count
from collections import OrderedDict
from django.template import RequestContext
from django.core import exceptions

import html2text
register = template.Library()
from cms.models.pagemodel import Page

@register.filter()
def list04(instance):
	# t = template.loader.get_template('list04_template.html')
	# context_dict = OrderedDict()
	body_ = ''
	for line in html2text.html2text(instance.body).splitlines():
		if len(line.strip()) >= 1:
			line = line.strip()
			if "*" == line[0]:
				line_ = u"<li><b>%s</b></li>" % line[1:]
				body_ += line_
			else:
				line_ = u"<p style='margin-left:10p'>%s</p>" % line
				body_ += line_
		else:
			body_ += line
	return body_

@register.filter()
def tabs_01(instance):
	# t = template.loader.get_template('list04_template.html')
	# context_dict = OrderedDict()
	print instance.tag
	pages = Page.objects.filter(tagextension__tag=instance.tag)
	# pages = Page.objects.all()
	body_ = ''
# <li> <a href="" title=""></a> </li>#}

	for page in pages:
		title = page.get_title()
		url = page.get_absolute_url()
		# url = 'dd'
		html_ = u'<li> <a href="{url}" title="{title}">{title}</a></li>'.format(title=title, url=url)
		# html_ = u'<li> <a href="{title}" title="{title}"></a>{title}</li>'.format(title=title)

		body_ += html_

	return body_


@register.filter()
def rightbox(instance):
	pages = Page.objects.filter(tagextension__tag=instance.tag)
	body_ = ''

	for page in pages:

		title = page.get_title()
		url = page.get_absolute_url()
		id = page.id
		html_ = u'<li> <a href="{url}" title="{title}">{title}{id}</a></li>'.format(title=title, url=url, id=id)
		body_ += html_

	return body_

@register.filter()
def small_menu(current_page):
	html = u'<a href="{url}" title="{title}">&nbsp;&raquo;&nbsp;{title}</a>'.format(title=current_page.get_title(), url=current_page.get_absolute_url())
	for i in range(1, 10):
		parent = current_page.parent
		if parent is not None:
			html_ = u'<a href="{url}" title="{title}">&nbsp;&raquo;&nbsp;{title}</a>'.format(title=parent.get_title(), url=parent.get_absolute_url())
			html = html_ + html
			current_page = parent
		else:
			html = html.replace('&nbsp;&raquo;&nbsp;', '', 1)
			break
	return html


@register.filter()
def menu_1(current_page):
	html = u'<a href="{url}" title="{title}">&nbsp;&raquo;&nbsp;{title}</a>'.format(title=current_page.get_title(), url=current_page.get_absolute_url())
	for i in range(1, 10):
		parent = current_page.parent
		if parent is not None:
			html_ = u'<a href="{url}" title="{title}">&nbsp;&raquo;&nbsp;{title}</a>'.format(title=parent.get_title(), url=parent.get_absolute_url())
			html = html_ + html
			current_page = parent
		else:
			html = html.replace('&nbsp;&raquo;&nbsp;', '', 1)
			break
	return html

@register.filter()
def get_page_url_by_title(reverse_id):
	# page = Page.objects.filter(page_instance__title=title)
	# page = Page.get_title_obj(title)
	# page = Page.objects.get(id='home')
	try:
		page = Page.objects.get(reverse_id=reverse_id)
	except Page.DoesNotExist:
		return ''

	if page is not None:
		return page.get_absolute_url()
	else:
		return None

@register.filter()
def get_page_title_and_url(reverse_id):
	print 'xxxxxxxxx%s' % reverse_id
	html = u''
	# page = Page.objects.get(id=14)
	try:
		# page = Page.objects.filter(reverse_id__exact=reverse_id, languages='en')
		# page = Page.objects.get(id=15)
		page = Page.objects.get(reverse_id=reverse_id, languages='en')
	except Page.DoesNotExist:
		return ''
	except Page.MultipleObjectsReturned:
		return u'请注意！有多个页面带有相同reverse_id'

	if page is None:
		return None

	# for page_ in page:
	# 	url = page_.get_absolute_url()
	# 	title = page_.get_title()
	# 	html += u'<dt><a href="{url}">{title}</a></dt>'.format(url=url, title=title)
	url = page.get_absolute_url()
	title = page.get_title()
	html += u'<dt><a href="{url}">{title}</a></dt>'.format(url=url, title=title)
	return html



@register.filter()
def get_sub_page_title_and_url(reverse_id):
	html = u''
	# page = Page.objects.get(id=14)
	try:
		page = Page.objects.get(reverse_id=reverse_id, languages='en')
	except Page.DoesNotExist:
		return ''
	except Page.MultipleObjectsReturned:
		return u'多个页面带有相同reverse_id'
	if page is None:
		return None
	if page.children is None:
		return None
	for children in page.children.all():
		url = children.get_absolute_url()
		title = children.get_title()
		html_ = u"<dd><a href='{url}'>{title}</a></dd>".format(url=url, title=title)
		html += html_
	return html

