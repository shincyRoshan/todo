from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import Tasks
from .forms import TodoForms
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView
# Create your views here.
def home(request):

    task = Tasks.objects.all()
    if request.method=="POST":
        name=request.POST.get('name','')
        priorites = request.POST.get('priority','')
        date = request.POST.get('date','')
        todo = Tasks(name=name, priority=priorites,date=date)
        todo.save()
    return render(request, 'home.html',{'tasks':task})
def delete(request,taskid):
    task=Tasks.objects.get(id=taskid)
    if request.method=="POST":
        task.delete()
        return redirect('/')
    return render(request,'delete.html')
def update(request,id):
    task = Tasks.objects.get(id=id)
    f=TodoForms(request.POST or None,instance=task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,'edit.html',{'f':f,'task':task})


class TaskListView(ListView):
    model=Tasks
    template_name = 'home.html'
    context_object_name = 'tasks'

class TaskDetailView(DetailView):
    model = Tasks
    template_name = 'details.html'
    context_object_name = 'task'

class TaskupdateView(UpdateView):
    model = Tasks
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('name','priority','date')




    def get_sucess_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})

class TaskDeleteView(DeleteView):
    model = Tasks
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvhome')



# def details(request):
    # task=Tasks.objects.all()

    # return render(request, 'details.html',{'tasks':task})