from django.forms import ModelForm
from .models import Services


class CustomModelForm(ModelForm):
    class Meta:
        model = Services
        fields = ('image',
                  'title',
                  'sub_title',
                  'author',
                  )

