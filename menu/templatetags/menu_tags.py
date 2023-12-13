from django import template

from menu.models import MenuItem

register = template.Library()


@register.inclusion_tag('menu_template.html', takes_context=True)
def show_menu(context, name):
    menu_items = MenuItem.objects.all()

    # Создание словарей для быстрого доступа к элементам меню по URL, названию, id
    url_dict = {item.url: item for item in menu_items}
    name_url_dict = {item.title: item.url for item in menu_items}
    id_item_dict = {item.id: item for item in menu_items}

    # Получение элемента меню по URL
    url = context.get('url')
    current_item_by_path_url = url_dict.get(url)

    current_url = name_url_dict.get(name)
    current_item = url_dict.get(current_url)

    if not current_item_by_path_url:
        return {'hierarchy': {current_item: {}}}

    parents_current_item_by_path_url = get_all_parents(url_dict, current_item_by_path_url.url, id_item_dict)
    parent = parents_current_item_by_path_url[0] if parents_current_item_by_path_url else current_item_by_path_url

    if parent.title != name:
        return {'hierarchy': {current_item: {}}}

    # Если у текущего элемента есть дочерние элементы, установим последний из них
    if current_item_by_path_url.get_children(menu_items):
        current_item_by_path_url = current_item_by_path_url.get_children(menu_items)[-1]

    # Получение родительских элементов для текущего элемента меню
    parents = get_all_parents(url_dict, current_item_by_path_url.url, id_item_dict)
    return {'hierarchy': get_dict(parents, menu_items)}

@register.inclusion_tag('menu_template.html')
def show_sub_menu(children):
    return {'hierarchy': children}
#from test1.templatetags.menu_tags import show_menu

def get_dict(parents,menu_items):
    """Создание вложенных словарей для отображения иерархии меню"""
    dict = {}
    prev = None
    for item in parents[::-1]:
        dict[item] = {value: dict[prev] if prev == value else {} for value in item.get_children(menu_items)}
        prev = item
    return {parents[0]:dict[prev]}

def get_all_parents(url_dict, url,id_item_dict):
    """Получение всех родительских элементов для заданного URL"""
    parents = []
    current_item = url_dict.get(url)
    while current_item.parent_id:
        parent = id_item_dict.get(current_item.parent_id)
        parents.append(parent)
        current_item = url_dict.get(parent.url)
    return parents[::-1]



