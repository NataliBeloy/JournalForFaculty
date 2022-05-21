from django import forms

from mailing.models import Mailing


class MailingCreateForm(forms.ModelForm):
    class Meta:
        model = Mailing
        fields = ['name', 'subject', 'message', 'to_users']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Назва розсилки'}),
            'subject': forms.TextInput(attrs={'placeholder': 'Заголовок повідомлення'}),
            'message': forms.Textarea(attrs={'placeholder': 'Текст повідомлення'}),
        }
