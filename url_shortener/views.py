from django.shortcuts import render, redirect
from django import forms
from django.http import HttpResponse, HttpResponseNotFound
import string, random
from models import ShortenedURL


class URLForm(forms.ModelForm):
    class Meta:
        model = ShortenedURL
        fields = ['original_url']

# generates random alphanumeric ending
def random_ending(length=6):
    choices = string.ascii_uppercase + string.ascii_lowercase + string.digits
    ending = ''.join(random.choice(choices) for _ in range(length))
    return ending

# generates random alphanumeric ending and makes sure no urls are already shortened to it
def unique_random_ending(length=6):
    ending = random_ending(length)
    while len(ShortenedURL.objects.filter(shortened_url=ending)) != 0:
        ending = random_ending(length)
    return ending

def index(request):
    return redirect('/new')

def new_url(request):
    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            shortened = unique_random_ending()
            obj.shortened_url = shortened
            obj.save()
            full_shortened = 'http://{}/{}'.format(request.META['HTTP_HOST'], shortened)
            return render(request, 'shortened_result.html', {'url': full_shortened})
    else:
        form = URLForm()
        return render(request, 'new_shortened.html', {'form': form})


def shortened_url(request):
    ending = request.path.split('/')[-1]
    objs = ShortenedURL.objects.filter(shortened_url=ending)
    print(ending)
    if len(objs) == 0:
        return HttpResponseNotFound('<h1>Shortened URL not found</h1>')
    else:
        original_url = objs[0].original_url
        return redirect(original_url)
