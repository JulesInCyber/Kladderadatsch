def make_tag(text: str, tag: str = "p", css_class: str = None) -> str:
    if css_class != None:
        html_string = f"<{tag} class='{css_class}'>{text}</{tag}>"
    else:
        html_string = f"<{tag}>{text}</{tag}>"
    return html_string

print(make_tag("Hello"))
print(make_tag("Title", "h1"))
print(make_tag("Note", css_class="hint"))
print(make_tag(tag="li", text="Milk"))
