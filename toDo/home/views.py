from django.shortcuts import render,redirect
from home.models import todoList
# Create your views here.
def indexPage(request):
    emp=todoList.objects.all()
    context={
        'emp':emp
    }
    return render(request,"index.html",context)

def addToDo(request):
    if request.method=="POST":
        inputs=request.POST.get('inputs')
        emp=todoList(
            item=inputs,
        )
        emp.save()
    return redirect(indexPage)

def deleteToDo(request,id):
    emp=todoList.objects.filter(id=id)
    emp.delete()
    context={
        'emp':emp
    }
    return redirect(indexPage)

def finishedToDo(request,id):
    items=todoList.objects.get(id=id)
    items.status="Finished"
    items.save()
    return redirect(indexPage)

def deleteAllToDo(request):
    items=todoList.objects.all()
    items.delete()
    return redirect(indexPage)
