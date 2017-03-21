#coding:utf-8

from django.shortcuts import render
from .user import User
from django import forms

class InputForm(forms.Form):
    a=forms.CharField()

# Create your views here.
def form(request):
    a={'1':1,'2':2,'3':3,'4':4,'5':5}
    b={'a':'a','b':'b','c':'c','d':'d','e':'e'}
    return render(request,"form.html",{'a1':a,'b1':b})

def index(request):
    if (request.method=='POST'):
        username=request.POST['username']
        if type(username)=="<type 'unicode'>":
            username=username.encode('utf-8')
        #print username
        newuser,sum,heros=stats(username)
        sum_avg={}
        for key,value in sum.items():
            sum_avg[key]=value/newuser.user_info['totalplays']

        sorted_heros={}
        for h in sorted(heros)[:6]:
            sorted_heros[h]=heros[h]

        print sum_avg
        print sorted_heros

        return render(request,'show_resault.html',{'sum':sum_avg,'heros':sorted_heros})
    #return HttpResponse('hehe')
    else:
        return render(request,"index.html")

def stats(name):
    newuser = User(name.strip())
    #print newuser.user_info
    #print newuser.match_info
    #print '\n'
    sum = {'kills':0,'dies':0,'helps':0,'buildings':0\
           ,'soldiers':0,'golds':0}
    heros={}
    for mi in newuser.match_info:
        #print mi
        #print mi['kills']
        kill=mi['kills'].split('/')
        #print kill
        sum['kills'] = sum['kills']+int(kill[0])
        sum['dies'] = sum['dies'] + int(kill[1])
        sum['helps'] = sum['helps'] + int(kill[2])
        sum['buildings']=sum['buildings']+mi['buildings']
        sum['soldiers']=sum['soldiers']+mi['soldiers']
        sum['golds']=sum['golds']+mi['golds']
        hero=mi['hero'].strip().encode('utf8')
        if heros.has_key(hero):
            heros[hero]=heros[hero]+1
        else:
            heros[hero]=1
    print sum['kills']
    print heros

    return newuser,sum,heros

