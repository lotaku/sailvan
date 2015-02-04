# encoding: utf-8
from django import forms
from django.core.urlresolvers import reverse
from django.db.models import Q


class UrlForm(forms.Form):


	type_first = forms.IntegerField()
	menu_level = forms.IntegerField()
	common_widget_id =  forms.IntegerField()
	parent_id =  forms.IntegerField()
	urls = forms.CharField(widget=forms.Textarea())

	def __init__(self,*args, **kwargs):
		super(UrlForm, self).__init__(*args, **kwargs)

		# self.fields['tags'].label = ""
		# self.fields['tags'].initial = [tag.id for tag in tags]
		# self.fields['tags'].required = False
		# self.fields['tags'].widget.attrs.update({'class': 'multicomplete',
		# 										 'callback': reverse('core_ajax_tag_lookup')})

	# def save(self):
	# 	return self.cleaned_data['tags']