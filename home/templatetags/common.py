from django import template

register = template.Library() 

@register.filter(name='is_editor') 
def is_editor(user):
    return user.groups.filter(name="editor").exists() 