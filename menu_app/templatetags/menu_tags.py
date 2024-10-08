
from django import template
from menu_app.models import MenuItem, Menu
import logging

logger = logging.getLogger(__name__)

register = template.Library()

@register.inclusion_tag('menu_app/menu.html', takes_context=True)
def draw_menu(context, menu_slug):
    request = context.get('request')
    current_path = request.path

    try:
        menu = Menu.objects.get(slug=menu_slug)
        menu_items = MenuItem.objects.filter(menu=menu).select_related('parent').prefetch_related('children')
        menu_tree = build_menu_tree(menu_items)
        active_item = find_active_item(menu_items, current_path)
        open_items = get_open_items(active_item)
    except Menu.DoesNotExist:
        logger.error(f"Menu with slug '{menu_slug}' does not exist.")
        menu_tree = []
        open_items = []
    except Exception as e:
        logger.error(f"Error fetching menu items: {e}")
        menu_tree = []
        open_items = []

    return {
        'menu_items': menu_tree,
        'current_path': current_path,
        'open_items': open_items,
    }


 

def build_menu_tree(menu_items):
    menu_dict = {item.id: item for item in menu_items}
    for item in menu_items:
        item.children_items = []
    root_items = []
    for item in menu_items:
        if item.parent_id:
            parent = menu_dict.get(item.parent_id)
            if parent:
                parent.children_items.append(item)
        else:
            root_items.append(item)
    return root_items

def find_active_item(menu_items, current_path):
    for item in menu_items:
        if item.get_absolute_url() == current_path:
            return item
    return None

def get_open_items(active_item):
    open_items = []
    if active_item:
        # Добавляем всех родителей в список открытых пунктов
        parent = active_item.parent
        while parent:
            open_items.append(parent.id)
            parent = parent.parent
        # Добавляем сам активный пункт
        open_items.append(active_item.id)
        # Добавляем детей активного пункта (первый уровень вложенности)
        for child in active_item.children.all():
            open_items.append(child.id)
    return open_items

