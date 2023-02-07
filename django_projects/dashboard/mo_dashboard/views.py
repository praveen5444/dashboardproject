from django.shortcuts import render
from django.http import HttpResponse
import csv
# Create your views here.
def todolist(request):
    context = {
        'welcome_text':"welcome to first page",
        }
    #return HttpResponse("Welcome to my page bro")
    #return render(request,'js/second.html',{})
    return render(request,'js/second.html',context)
    #return render(request,'first.html',{})

def curam(request):
     
    context = {
        'welcome_text':"welcome to curam page",
    }
    #myname={'firstkey': [['sit1', '2pm', 'uat'], ['sit2', '3pm', 'stage'], ['sit3', '4pm', 'prod']]}
    myname={}
    #return HttpResponse("Welcome to my page bro")
    #return render(request,'js/third.html',{})
    #with open("curaminputdata", "r") as csvfile:
    with open('curaminputdata','r') as file:
        to_return = []
        a = file.read().splitlines()
        for tab in a:
            tab = tab.split('|')
            to_return.append(tab)
    myname={'firstkey':to_return}
            
            #reader = csv.reader(csvfile, delimiter='|')
            #for row in reader:
                #print(row)
                #print(row[0])
                #a=row[0]
                #b=row[1]
                #c=row[2]

                
                #z['first':a,'second':b,'third':c]
                #z['first']=a
                #z['second']=b
                #z['third']=c
                #print(z)
                
                #print(row[1])
    #return HttpResponse(a)            
    #return render(request,'js/third.html',context)
    print(myname)
    return render(request,'js/third.html',myname)
    #return render(request,'first.html',{})
def ua(request):
    context = {
        'welcome_text':"welcome to ua page"
    }
    #return HttpResponse("Welcome to my page bro")
    return render(request,'js/four.html',context)
    #return render(request,'first.html',{})
    