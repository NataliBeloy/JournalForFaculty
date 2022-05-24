from django.contrib import admin
from django.utils.safestring import mark_safe

from people.models import User, Teacher, Student, Contact


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Користувачі."""
    list_display = ['get_full_name', 'sex', 'user_status', 'username', 'get_image']
    list_filter = ('user_status',)
    search_fields = ('get_full_name', 'username')
    save_on_top = True
    fields = ('date_joined', 'last_login', 'username', 'password', 'email', 'user_status', 'first_name', 'last_name',
              'middle_name', 'birth_date', 'sex', 'photo', 'description', 'is_superuser', 'is_staff',
              'is_active', 'user_permissions', 'groups')
    readonly_fields = ('date_joined', 'last_login')

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.photo.url} width="30" height="30"')

    def get_full_name(self, obj):
        return f'{obj.last_name} {obj.first_name} {obj.middle_name}'

    get_image.short_description = 'Зображення'
    get_full_name.short_description = 'Повне ім\'я'
    get_full_name.admin_order_field = 'last_name'


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    """Викладачі."""
    list_display = ('get_full_name', 'group_manager', 'position', 'user', 'education', 'study_work', 'science_work', )
    list_filter = ('group_manager',)
    search_fields = ('get_full_name',)

    def get_full_name(self, obj):
        return f'{obj.user.last_name} {obj.user.first_name} {obj.user.middle_name}'

    get_full_name.short_description = 'Повне ім\'я'


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    """Студенти."""
    list_display = ('get_full_name', 'group', 'user', 'study_form', 'study_degree', 'entry_year', 'course_work',
                    'course_supervisor', 'diploma_work', 'diploma_supervisor', )
    list_filter = ('group',)
    search_fields = ('get_full_name',)

    def get_full_name(self, obj):
        return f'{obj.user.last_name} {obj.user.first_name} {obj.user.middle_name}'

    get_full_name.short_description = 'Повне ім\'я'


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """Контакти."""
    list_display = ('get_full_name', 'phone1', 'phone2', 'phone3')

    def get_full_name(self, obj):
        return f'{obj.user.last_name} {obj.user.first_name} {obj.user.middle_name}'

    get_full_name.short_description = 'Повне ім\'я'
