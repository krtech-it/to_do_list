from django.shortcuts import render
from .models import TodoListItem
from django.http import HttpResponseRedirect
from django.urls import reverse

def todoappView(request):
    todoList = TodoListItem.objects.all()
    return render(request, 'todolist.html', {'todoList': todoList})

def addTodoView(request):
    x = request.POST['content']
    new_item = TodoListItem(content=x)
    new_item.save()
    return HttpResponseRedirect(reverse('home'))

def deleteTodoView(request, pk):
    y = TodoListItem.objects.get(id=pk)
    y.delete()
    return  HttpResponseRedirect(reverse('home'))
