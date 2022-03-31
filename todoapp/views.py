from django.shortcuts import render, redirect
from .models import TodoModel

def TodoView(request):
    if request.method == 'POST':
        data = request.POST
        blog = TodoModel.objects.create(title = data['title'], author = request.user)
        blog.save()
    def get_queryset():
        if request.user.is_superuser:
            return TodoModel.objects.all()
        else:
            return TodoModel.objects.all().filter(author=request.user)
    context = {
        'article': get_queryset()
    }
    return render(request, 'todo.html', context)

def delete_post(request,post_id=None):
    post_to_delete= TodoModel.objects.get(id=post_id)
    post_to_delete.delete()
    return redirect('main:index')