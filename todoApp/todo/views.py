from django.shortcuts import render, redirect,get_object_or_404
from .models import Todo
from .forms import TodoForm

def main(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user  # Associate the task with the logged-in user
            todo.save()
            return redirect('main')  # Redirect back to the same page after saving

    else:
        form = TodoForm()  # Create an empty form for GET requests

    # Fetch tasks for the authenticated user
    if request.user.is_authenticated:
        tasks = Todo.objects.filter(user=request.user).order_by('-id')
    else:
        tasks = Todo.objects.none()

    # Pass both the form and tasks to the template
    return render(request, 'main.html', {'form': form, 'tasks': tasks})


def todo_delete(request,todo_id):
    todo=get_object_or_404(Todo,user=request.user,pk=todo_id)
    if request.method=="POST":
        todo.delete()
        return redirect('main')
    
    return render(request,'todo_confirm_delete.html',{"todo":todo})

def todo_edit(request,todo_id):
    todo=get_object_or_404(Todo,user=request.user,pk=todo_id)
    # print(request.user)
    if request.method=="POST":
        form=TodoForm(request.POST,request.FILES,instance=todo)

        if form.is_valid():
            todo=form.save(commit=False)
            todo.user=request.user
            todo.save()
            return redirect('main')
    else:
            form=TodoForm(instance=todo)
    return render(request,'todo_form.html',{'form':form})


