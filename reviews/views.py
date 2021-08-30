from django.shortcuts import render


def index(request):
    name = "world"
    return render(request, "base.html", {"name": name})

def book_search(request):
    search_item = request.GET.get("search", "")
    return render(request, "search_results.html", {"search_item": search_item})
