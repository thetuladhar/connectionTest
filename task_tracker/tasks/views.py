from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Task
from .forms import TaskForm

class TaskListView(View):
    template_name = 'tasks.html'

    def get(self, request, *args, **kwargs):
        tasks = Task.objects.all()
        form = TaskForm()
        return render(request, self.template_name, {'tasks': tasks, 'form': form})

class TaskDetailView(View):
    template_name = 'tasks.html'

    def get(self, request, pk, *args, **kwargs):
        task = get_object_or_404(Task, pk=pk)
        form = TaskForm(instance=task)
        return render(request, self.template_name, {'task': task, 'form': form})

class TaskCreateView(View):
    template_name = 'tasks.html'

    def post(self, request, *args, **kwargs):
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')

        tasks = Task.objects.all()
        return render(request, self.template_name, {'tasks': tasks, 'form': form})

class TaskUpdateView(View):
    template_name = 'tasks.html'

    def post(self, request, pk, *args, **kwargs):
        task = get_object_or_404(Task, pk=pk)
        form = TaskForm(request.POST, instance=task)
        
        if form.is_valid():
            form.save()
        # Move the rendering outside the is_valid() block
        tasks = Task.objects.all()
        return render(request, self.template_name, {'tasks': tasks, 'form': form})

class TaskDeleteView(View):
    template_name = 'tasks.html'

    def post(self, request, pk, *args, **kwargs):
        task = get_object_or_404(Task, pk=pk)
        task.delete()
        # Move the rendering outside the is_valid() block
        form = TaskForm()
        tasks = Task.objects.all()
        return render(request, 'tasks.html', {'tasks': tasks, 'form': form})

class UpdateTaskStatusView(View):
    def post(self, request, pk, *args, **kwargs):
        task = get_object_or_404(Task, pk=pk)
        new_status = request.POST.get('status')

        if new_status:
            task.status = new_status
            task.save()

        return redirect('task_list')
