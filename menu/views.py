from django.shortcuts import render

# Create your views here.
def menu_view(request, url=None):
    return render(request, 'menu_page.html',{'url': url})