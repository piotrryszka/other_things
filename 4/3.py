def tag(name, *content, cls=None, **attrs):
    """Generowanie co najmniej jednego znacznika HTML"""
    if cls is not None:
        attrs['class'] = cls
    if attrs:
        attr_str = ''.join(' %s="%s"' % (attr, value)
                           for attr, value
                           in sorted(attrs.items()))
    else:
        attr_str = ''
    if content:
        return '\n'.join('<%s%s>%s</%s>' %
                         (name, attr_str, c, name) for c in content)
    else:
        return '<%s%s />' % (name, attr_str)


# print(tag('br'))
# print(tag('p', 'hello'))
# print(tag('p', 'hello', 'world'))
# print(tag('p', 'hello', 'world', id=33))
# print(tag('p', 'hello', cls='header'))
# print(tag(content='test', name="img"))
#
# my = {'name': 'img', 'title': 'Kurs Python', 'src': 'sunset.jpg', 'cls': 'div'}
#
# print(tag(**my))

def f(a, *, b):
    return a, b

print(f(1,b=2))
