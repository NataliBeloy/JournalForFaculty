from django import forms
from django.forms.models import modelformset_factory

from .models import Student, Contact, User


class UserCreateForm(forms.ModelForm):
    """Форма створення нового користувача."""
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'middle_name',
                  'birth_date', 'sex', 'photo', 'description']
        widgets = {'username': forms.TextInput(attrs={'placeholder': 'Ім\'я користувача'}),
                   'email': forms.EmailInput(attrs={'placeholder': 'E-mail'}),
                   'password': forms.PasswordInput(attrs={'placeholder': 'Пароль'}),
                   'first_name': forms.TextInput(attrs={'placeholder': 'Ім\'я'}),
                   'last_name': forms.TextInput(attrs={'placeholder': 'Прізвище'}),
                   'middle_name': forms.TextInput(attrs={'placeholder': 'По-батькові'}),
                   'birth_date': forms.DateInput(attrs={'placeholder': 'Дата народження', 'type': 'date'}),
                   'sex': forms.Select(attrs={'placeholder': 'Стать'}),
                   'photo': forms.FileInput(attrs={'class': 'input-file'}),
                   'description': forms.Textarea(attrs={'placeholder': 'Характеристика', 'rows': 5, 'cols': 30}),

                   }

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class UserUpdateForm(forms.ModelForm):
    """Форма для оновлення даних користувача."""
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'middle_name',
                  'sex', 'birth_date', 'photo', 'description']
        widgets = {'first_name': forms.TextInput(attrs={'placeholder': 'Ім\'я'}),
                   'last_name': forms.TextInput(attrs={'placeholder': 'Прізвище'}),
                   'middle_name': forms.TextInput(attrs={'placeholder': 'По-батькові'}),
                   'birth_date': forms.DateInput(attrs={'type': 'date', 'data-date-format': 'yyyy-mm-dd'},
                                                 format=('%Y-%m-%d')),
                   'sex': forms.Select(attrs={'placeholder': 'Стать'}),
                   'photo': forms.FileInput(attrs={'class': 'input-file'}),
                   'description': forms.Textarea(attrs={'placeholder': 'Характеристика', 'rows': 5, 'cols': 40}),
                   }


class StudentForm(forms.ModelForm):
    """Форма пов'язана з користувацькою формою, інформація про студента."""
    class Meta:
        model = Student
        fields = ('group', 'study_form', 'study_degree', 'entry_year', 'course_work', 'course_supervisor',
                  'diploma_work', 'diploma_supervisor', )
        widgets = {'group': forms.Select(),
                   'study_degree': forms.Select(attrs={'placeholder': 'Ступінь навчання'}),
                   'entry_year': forms.TextInput(attrs={'placeholder': 'Рік вступу'}),
                   'study_form': forms.Select(attrs={'placeholder': 'Форма навчання'}),
                   'course_work': forms.TextInput(attrs={'placeholder': 'Тема курсової роботи'}),
                   'course_supervisor': forms.Select(attrs={'placeholder': 'Керівник курсової роботи'}),
                   'diploma_work': forms.TextInput(attrs={'placeholder': 'Тема дипломної роботи(бакалавр)'}),
                   'diploma_supervisor': forms.Select(attrs={'placeholder': 'Керівник дипломної роботи(бакалавр)'}),
                   }


class ContactForm(forms.ModelForm):
    """Форма пов'язана з користувацькою формою, контактні дані."""
    class Meta:
        model = Contact
        fields = ['phone1', 'phone2', 'phone3']
        widgets = {'phone1': forms.TextInput(attrs={'placeholder': 'Телефон'}),
                   'phone2': forms.TextInput(attrs={'placeholder': 'Додатковий телефон'}),
                   'phone3': forms.TextInput(attrs={'placeholder': 'Додатковий телефон №2'}),

                   }


ContactFormSet = modelformset_factory(Contact, form=ContactForm, max_num=1, extra=1)
StudentFormSet = modelformset_factory(Student, form=StudentForm, max_num=1, extra=1)
