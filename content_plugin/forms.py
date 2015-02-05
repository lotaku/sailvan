from django import forms
from .models import IndexContentBoxPlugin3


class BoxForm(forms.ModelForm):

    class Meta:
        "Fields Form"
        model = IndexContentBoxPlugin3
        # fields = ('index_content_box.title', 'index_content_box.order', )