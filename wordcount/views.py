from django.http import HttpResponse
from django.shortcuts import render

#def homepage(request):
    #return HttpResponse("Hello World")


def about(request):
    return render(request,'about.html')

def contact(request):
    return HttpResponse("This is contact page")

def home(request):
    return render(request,'home.html')


def count(request):
    data=request.GET['fulltext']
    word_list=data.split()
    list_len=len(word_list)
    word_dict={}
    for word in word_list:
        if word in word_dict:
            word_dict[word]+=1
        else:
            word_dict[word]=1



    return render(request,'count.html',{'full':data, 'words':list_len,'word_count':word_dict})
