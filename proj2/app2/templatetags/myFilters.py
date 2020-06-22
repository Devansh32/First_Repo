from django import template

register = template.Library()

def cut(value,arg):
    #cuts out all instances of arg from value
    return value.replace(arg,'')



register.filter('cut',cut)


