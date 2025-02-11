from django.forms import ModelForm
from django import forms
from .models import Services,SliderOne,SliderTwo,Contact


# Admin panel theke sob handle korle form lagbe na
class CustomModelForm(forms.ModelForm):
    class Meta:
        model = Services
        fields = ('image',
                  'title',
                  'sub_title',
                  'author',
                  )
        
class SliderOneModelForm(forms.ModelForm):
    class Meta:
        model = SliderOne
        fields = ('image',
                  'title',
                  'sub_title',
                  'author',
                  )

class SliderTwoModelForm(forms.ModelForm):
    class Meta:
        model = SliderTwo
        fields = ('image',
                  'name',
                  'title',
                  'sub_title',
                  'author',
                  )
# Admin panel theke sob handle korle form lagbe na
                    # END       



class ContactModelForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name',
                  'subject',
                  'phone',
                  'email',
                  'message',
                  )


