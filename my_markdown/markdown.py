from markdown import markdown

def markdown_to_html(md):
    html = markdown(md)
    return html