import jinja2
from jinja2 import PackageLoader

text = jinja2.Template("foo", autoescape=True)

env = jinja2.Environment(autoescape=True)

env = jinja2.Environment(autoescape=True)

env = jinja2.Environment(
    loader=PackageLoader('yourapplication', 'templates'),
    autoescape=True
)

env = jinja2.Environment(
    loader=PackageLoader('yourapplication', 'templates'), autoescape=True
)