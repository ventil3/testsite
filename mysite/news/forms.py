from django import forms
from .models import Category, News


#форма, несвязанная с моделью
# class NewsForm(forms.Form):
#     title = forms.CharField(max_length=150, label='Заголовок ', widget=forms.TextInput(attrs={'class': 'form-control'}))
#     content = forms.CharField(label='Текст ', required=False, widget=forms.Textarea(attrs={'class': 'form-control',
#                                                                                            'rows': 5
#                                                                                            }))
#     is_published = forms.BooleanField(label='Опубликовано? ', initial=True)
#     category = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категория ', empty_label='Выберите '
#                                                                                                        'категорию',
#                                       widget=forms.Select(attrs={
#         'class': 'form-control'
#     }))


#форма, связанная с моделью
class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        # fields = '__all__'
        fields = ['title', 'content', 'is_published', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'})
        }
