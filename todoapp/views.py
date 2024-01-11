from django.http import request
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from todoapp.forms import Todoform
from todoapp.models import Task


class Tasklistview (ListView):
    model=Task
    template_name = 'home.html'
    context_object_name = 'task1'

class Taskdetailview (DetailView):
    model=Task
    template_name = 'detail.html'
    context_object_name = 'task'

class Taskdeleteview(DeleteView):
        model = Task
        template_name = 'delete.html'
        success_url=reverse_lazy('cbvhome')


class Taskdupdateview (UpdateView):
    model = Task
    template_name = 'edit.html'
    context_object_name = 'task'
    fields=('name','priority','date')
    def get_success_url(self):
          return (reverse_lazy('cbvdetail',kwargs={'pk':self.object.id} ) )


# Create your views here.
def add(request):
    task1 = Task.objects.all()
    if request.method =='POST':
        name = request.POST.get('task','')
        priority = request.POST.get('priority', '')
        date=request.POST.get('date', '')
        task=Task(name=name,priority=priority,date=date)
        task.save()
    return render(request,'home.html',{'task1':task1})


def delete(request , taskid):
    task = Task.objects.get(id=taskid)
    if request.method =='POST':
        task.delete()
        return redirect('/')
    return render(request, 'delete.html')


def update(request , id):
    task = Task.objects.get(id=id)
    f = Todoform(request.POST or None,instance=task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request, 'update.html',{'f':f,'task':task})


