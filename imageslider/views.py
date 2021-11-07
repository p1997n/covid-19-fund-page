from django.shortcuts import render
import requests

def showing(request):
    return render(request,'index.html')


def home(request):
    response=requests.get('https://www.itukama.lk/wp-content/plugins/revslider/public/assets/js/extensions/revolution.extension.slideanims.min.js?version=5.3.1.4').json()
    return render(request,'index.html',{'response':response})
