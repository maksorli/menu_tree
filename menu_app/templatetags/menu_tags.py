
from django import template
from menu_app.models import MenuItem
import logging

logger = logging.getLogger(__name__)

register = template.Library()

@register.inclusion_tag('menu_app/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    logger.debug(f"draw_menu called with menu_name={menu_name}")
    print(f"draw_menu called with menu_name={menu_name}")
    
    request = context.get('request')
    if not request:
        logger.debug("Request object not found in context")
        print("Request object not found in context")
        return {'menu_items': [], 'current_path': ''}
    
    current_path = request.path
    logger.debug(f"Current path: {current_path}")
    print(f"Current path: {current_path}")
    
    try:
        menu_items = MenuItem.objects.filter(menu_name=menu_name).select_related('parent').prefetch_related('children')
        logger.debug(f"Menu items: {menu_items}")
        print(f"Menu items: {menu_items}")
    except Exception as e:
        logger.error(f"Error fetching menu items: {e}")
        print(f"Error fetching menu items: {e}")
        return {'menu_items': [], 'current_path': current_path}
    
    menu_tree = build_menu_tree(menu_items)
    return {
        'menu_items': menu_tree,
        'current_path': current_path,
    }


@register.simple_tag
def test_tag():
    return "Test Tag Output"

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
