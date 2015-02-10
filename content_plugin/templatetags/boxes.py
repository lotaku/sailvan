# -*- coding: UTF-8 –*-
# from coffin import template
from django import template
import re
import html2text
register = template.Library()
from cms.models.pagemodel import Page


@register.filter()
def menu_2(instance):
	html = u'''
				<div>
					{img}
					<dl>
						{title}
						{menu}
					</dl>
					<div class="clear"></div>
				</div>

			'''
	menu_html = u'''<dd><a href="{menu_url}">{menu_title}</a></dd>'''
	title_html = u'''<dt><a href="{title_url}">{title}</a></dt>'''
	img_html = u'''
		<dl>
		<img src="{MEDIA_URL}{img}"/>
		</dl>
	'''
	if instance.coverImg:
		img_html = img_html.format(MEDIA_URL='/media/', img=instance.coverImg)
	else:
		img_html = ''

	try:
		page = Page.objects.get(reverse_id=instance.reverse_id, publisher_is_draft=1)
	except Page.DoesNotExist:
		return html

	title_html = title_html.format(title_url=page.get_absolute_url(), title=page.get_title())
	print page.get_absolute_url()
	if not page.children:
		return html.format(img=img_html, title=title_html, menu=menu_html)

	menu_html_result = ''
	for children in page.children.all():
		menu_html_ = menu_html.format(menu_url=children.get_absolute_url(), menu_title=children.get_title())
		menu_html_result += menu_html_

	html = html.format(img=img_html, title=title_html, menu=menu_html_result)

	return html


@register.filter()
def body_stowable(instance):
	body = instance.body
	whole_body = re.sub(u'#以下隐藏#', '', body)
	whole_body = re.sub(u"\r\n", u"<br>", whole_body)
	whole_body = re.sub(u"<p>|</p>", u"", whole_body)
	whole_body = re.sub(u"<br><br><br>", u"<br>", whole_body)
	body_list = re.split(u'#以下隐藏#', instance.body)
	showed_body = body_list[0]
	body_ = u"\
			<div class='pt20 intro1' style='display: block;'>{showed_body}</div>\
			<div class='pt20 intro2' style='display: none;'>{hidden_body}</div>\
			<a class='btn fr' href='#1'>详细&gt;&gt;</a>\
			<div class='bor'></div>\
			".format(showed_body=showed_body, hidden_body=whole_body)
	return body_

@register.filter()
def body_common(instance):

	html = u'''
			<div class="pt20">
				{body}
			</div>
			'''.format(body=instance.body)

	if instance.show_dividing_line:
		dividing_line = u'<div class="bor"></div>'
		html += dividing_line

	return html


@register.filter()
def list04(instance):
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
	print instance.tag
	pages = Page.objects.filter(tagextension__tag=instance.tag)
	body_ = ''
	for page in pages:
		title = page.get_title()
		url = page.get_absolute_url()
		html_ = u'<li> <a href="{url}" title="{title}">{title}</a></li>'.format(title=title, url=url)
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
	try:
		page = Page.objects.get(reverse_id=reverse_id, publisher_is_draft=1)
	except Page.DoesNotExist:
		return ''

	if page is not None:
		return page.get_absolute_url()
	else:
		return None


@register.filter()
def get_page_title_and_url(reverse_id):
	html = u''
	try:
		page = Page.objects.get(reverse_id=reverse_id, publisher_is_draft=1)
	except Page.DoesNotExist:
		return ''
	except Page.MultipleObjectsReturned:
		return u'请注意！有多个页面带有相同reverse_id'

	if page is None:
		return None

	url = page.get_absolute_url()
	title = page.get_title()
	html += u'<dt><a href="{url}">{title}</a></dt>'.format(url=url, title=title)
	return html


@register.filter()
def get_sub_page_title_and_url(reverse_id):
	html = u''
	try:
		page = Page.objects.get(reverse_id=reverse_id, publisher_is_draft=1)
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


@register.filter()
def show_sub_page_in_post(reverse_id):
	html = u''
	try:
		page = Page.objects.get(reverse_id=reverse_id, publisher_is_draft=1)
	except Page.DoesNotExist:
		return ''
	except Page.MultipleObjectsReturned:
		return u'请注意！有多个页面带有相同reverse_id'

	if page is None:
		return None
	if page.children is None:
		return None
	for children in page.children.all():
		url = children.get_absolute_url()
		title = children.get_title()
		brief = children.tagextension.brief
		if len(brief) <= 0:
			brief = u'该页面没有简介'

		# 是否显示为列表
		brief_ = ''
		for line in brief.split('\r\n'):
			old_line = line
			line = re.sub(u"<p>|</p>", u"", line)
			print line
			if len(line) >= 1 and line.strip()[0] == '*':
				line = line[1:]
				line_ = "<dd>{line}</dd>".format(line=line)
				brief_ += line_
			else:
				brief_ += old_line
		if brief_:
			brief = brief_
		html += u'''<dl class="list_03">
						<dt><a href="{url}">{title}</a></dt>
						{brief}
						<a class="more" href="{url}">详细&gt;&gt;</a>
					</dl>'''.format(url=url, title=title, brief=brief)
	return html


