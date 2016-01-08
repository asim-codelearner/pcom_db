from django import template

register = template.Library()

@register.filter(name='add_css_to_form')
def add_css_form(field, css):
	attrs = {}
	print(css)
	definition = css.split(',')
	print(definition)
	for d in definition:
		if ':' in d:
			t, v = d.split(':')
			attrs[t] = v
	
	return field.as_widget(attrs=attrs)