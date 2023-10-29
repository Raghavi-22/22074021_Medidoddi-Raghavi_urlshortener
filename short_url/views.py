from django.shortcuts import render, redirect
from .models import URL
from django.views.generic.list import ListView
from django.http import HttpResponseNotFound
def shorten_url(request):
    if request.method == 'POST':
        long_url = request.POST.get('long_url')
        if long_url:
            url, created = URL.objects.get_or_create(long_url=long_url)
            return render(request, 'short_url/shortened_url.html', {'short_url': url.short_code})

    return render(request, 'short_url/shorten_url.html')

def redirect_original(request, short_code):
    try:
        url = URL.objects.get(short_code=short_code)
        return redirect(url.long_url)
    except URL.DoesNotExist:
        pass


def url_list(request):
    urls = URL.objects.all()
    return render(request, 'short_url/url_list.html', {'urls': urls})