from django.shortcuts import render
from .models import ShortURL
from .forms import CreateNewShortURL
from datetime import datetime
import random, string

# Create your views here.
def home(request):
    return render(request, 'url_shortner/home.html')

def redirect(request, url):
    current_obj = ShortURL.objects.filter(shorturl=url)
    if len(current_obj) == 0:
        return render(request, 'url_shortner/pagenotfound.html')
    context = {'obj':current_obj[0]}
    return render(request, 'url_shortner/redirect.html', context)

def createShortURL(request):
    if request.method == 'POST':
        form = CreateNewShortURL(request.POST)
        if form.is_valid():
            original_website = form.cleaned_data['longurl']
            if (len(ShortURL.objects.filter(longurl=original_website))!=0):
                random_chars=ShortURL.objects.filter(longurl=original_website).first().shorturl
            else:
                random_chars_list = list(string.ascii_letters)
                random_chars=''
                for i in range(6):
                    random_chars += random.choice(random_chars_list)
                while len(ShortURL.objects.filter(shorturl=random_chars)) != 0:
                    for i in range(6):
                        random_chars += random.choice(random_chars_list)
                d = datetime.now()
                s = ShortURL(longurl=original_website, shorturl=random_chars, date_time=d)
                s.save()
            return render(request, 'url_shortner/urlcreated.html', {'chars':random_chars})
    
    else:
        form=CreateNewShortURL()
        context={'form': form}
        return render(request, 'url_shortner/create.html', context)