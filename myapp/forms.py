from django.forms import ModelForm
from .models import Services,SliderOne,SliderTwo,Contact


# Admin panel theke sob handle korle form lagbe na
class CustomModelForm(ModelForm):
    class Meta:
        model = Services
        fields = ('image',
                  'title',
                  'sub_title',
                  'author',
                  )
        
class SliderOneModelForm(ModelForm):
    class Meta:
        model = SliderOne
        fields = ('image',
                  'title',
                  'sub_title',
                  'author',
                  )

class SliderTwoModelForm(ModelForm):
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



class ContactModelForm(ModelForm):
    class Meta:
        model = Contact
        fields = ('name',
                  'subject',
                  'phone',
                  'email',
                  'message',
                  )


