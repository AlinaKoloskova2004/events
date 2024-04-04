from .models import Comment
from .forms import CommentForm
from django.shortcuts import render,  redirect

def add_comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.save()
            return render(request, 'activity/main.html', {'form': form})
    else:
        form = CommentForm()
    comments = Comment.objects.filter(approved_comment=True)
    return render(request, 'comment/add_comment.html', {'form': form, 'comments': comments})
