from mako.template import Template

t = Template("<html><body>${ input }</body></html>")

t.render(input="<script type='javascript'>alert('Hello from XSS!')</script>")
