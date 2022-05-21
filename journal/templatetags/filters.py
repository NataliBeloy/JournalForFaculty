from django.template.defaulttags import register


@register.filter(name='get_dict_value')
def get_dict_value(dictionary, key):
    """Отримує значення по ключу із словника."""
    return dictionary.get(key)


@register.filter(name='get_list_value')
def get_list_value(list_obj, num):
    """Отримує значення по індексу зі списку."""
    return list_obj[num]


@register.filter(name='is_member')
def is_member(user, group):
    """Перевіряє чи є користувач учасником групи."""
    return user.groups.filter(name=group).exists()

