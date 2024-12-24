from django.shortcuts import render

def home(request):
    tags = [
        {"name": "<h1>", "url": "h1"},
        {"name": "<p>", "url": "p"},
        {"name": "<a>", "url": "a"},
        {"name": "<ul>", "url": "ul"},
        {"name": "<ol>", "url": "ol"},
        {"name": "<li>", "url": "li"},
        {"name": "<div>", "url": "div"},
        {"name": "<span>", "url": "span"},
        {"name": "<table>", "url": "table"},
        {"name": "<img>", "url": "img"},
    ]
    return render(request, "tags/home.html", {"tags": tags})

def tag_detail(request, tag):
    descriptions = {
        "h1": "Defines the largest heading.",
        "p": "Defines a paragraph.",
        "a": "Defines a hyperlink.",
        "ul": "Defines an unordered list.",
        "ol": "Defines an ordered list.",
        "li": "Defines a list item.",
        "div": "Defines a division or section.",
        "span": "Defines a section inline.",
        "table": "Defines a table.",
        "img": "Defines an image.",
    }
    return render(request, "tags/tag_detail.html", {"tag": tag, "description": descriptions.get(tag, "No description available.")})
