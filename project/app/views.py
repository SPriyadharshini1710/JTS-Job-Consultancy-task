from django.shortcuts import render, get_object_or_404, redirect
from .models import Task

# View to display all tasks
def view_all_tasks(request):
    tasks = Task.objects.all()  # Fetch all tasks
    return render(request, 'view_all_tasks.html', {'tasks': tasks})

# Create a new task
def add_task(request):
    if request.method == 'POST':
        # Get data from the request and create a new Task instance
        title = request.POST.get('title')
        description = request.POST.get('description')
        priority = request.POST.get('priority')
        status = request.POST.get('status')

        # Create a new task instance
        Task.objects.create(
            title=title,
            description=description,
            priority=priority,
            status=status
        )
        return redirect('view_all_tasks')  # Redirect to the task list
    return render(request, 'add_task.html')  # Render the form for adding a task

# Update an existing task
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)  # Get the task by ID
    if request.method == 'POST':
        # Get data from the request and update the Task instance
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.priority = request.POST.get('priority')
        task.status = request.POST.get('status')
        task.save()  # Save the updated task
        return redirect('view_all_tasks')  # Redirect to the task list
    return render(request, 'edit_task.html', {'task': task})  # Render the edit form

# Delete a task
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)  # Get the task by ID
    task.delete()  # Delete the task from the database
    return redirect('view_all_tasks')  # Redirect to the task list
