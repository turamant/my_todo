from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView

from tasks.models import Task
from tasks.forms import TaskForm


class TaskView(ListView):
    '''
    Класс представление списка задач
    '''
    model = Task
    template_name = 'tasks/task_list.html'


class CreateTask(LoginRequiredMixin, CreateView):
    '''
        Класс представление создания новых задач, плюс миксин для
         разграничения доступа
    '''
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_create.html'
    success_url = '/todo/'
    login_url = 'login'

    def form_valid(self, form):
        '''метод проверки валидности формы'''
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdateTask(LoginRequiredMixin, UpdateView):
    '''
    Класс представление редактирования задач, плюс миксин для
             разграничения доступа
    '''
    model = Task
    form_class = TaskForm
    template_name = 'tasks/update_task.html'
    success_url = reverse_lazy('list')
    login_url = 'login'

    def form_valid(self, form):
        '''метод проверки валидности формы'''
        form.instance.author = self.request.user
        return super().form_valid(form)

class DeleteTask(LoginRequiredMixin, DeleteView):
    '''
    Класс представление удаления задач, плюс миксин для
             разграничения доступа
    '''
    model = Task
    template_name = 'tasks/delete.html'
    success_url = reverse_lazy('list')
    login_url = 'login'



'''
Для примера приведены контроллеры - функции
'''
#Контроллер - функция
def index(request):
    tasks = Task.objects.all()
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/todo/')
    return render(request, 'tasks/list.html', context={'tasks':tasks,
                                                       'form':form})

#Контроллер - функция
def update_task(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/todo/')
    return render(request, 'tasks/update_task.html', context={'form':form})



#Контроллер - функция
def delete(request, pk):
    item = Task.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('/todo/')
    return render(request, 'tasks/delete.html', context={'item':item})
