import re
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import CreateView, UpdateView
from .models import Idea
from .forms import IdeaForm
from .models import DevTool
from .forms import DevForm

def idea_list(request):
    qs = Idea.objects.all()

    q = request.GET.get('q','')
    if q:
        qs = qs.filter(name_icontains=q)

    return render(request, 'blog/idea_list.html', {
        'idea_list':qs,
        'q':q,
    })


def idea_detail(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
    return render(request, 'blog/idea_detail.html', {
            'idea': idea,
    })

def idea_delete(request, pk):
    idea = get_object_or_404(Idea, pk=pk)

    if request.method == "POST":
        idea.delete()
        return redirect("blog:idea_list")
    else:
        return redirect("blog:idea_detail", pk=idea.pk)

def idea_new(request):
    if request.method == "POST":
        form = IdeaForm(request.POST, request.FILES)
        if form.is_valid():
            idea = form.save()
            return redirect("blog:idea_detail", pk=idea.pk)
    else:
        form = IdeaForm()
        ctx = {
            "form": form
        }
        return render(request, "blog/idea_create.html", ctx)

def idea_update(request, pk):
    idea = get_object_or_404(Idea, pk=pk)

    if request.method == "POST":
        form = IdeaForm(request.POST, request.FILES, instance=idea)
        if form.is_valid():
            idea = form.save()
            return redirect("blog:idea_detail", pk=idea.pk)
    else:
        form = IdeaForm(instance=idea)
        ctx = {
            "form": form
        }
        return render(request, "blog/idea_update.html", ctx)


def devtool_list(request):
    qs = DevTool.objects.all()

    q = request.GET.get('q','')
    if q:
        qs = qs.filter(name_icontains=q)

    return render(request, 'blog/devtool_list.html', {
        'devtool_list':qs,
        'q':q,
    })

def devtool_detail(request, pk):
    devtool = get_object_or_404(DevTool, pk=pk)
    idea_list = devtool.ideas.all()
    return render(request, 'blog/devtool_detail.html', {
            'devtool': devtool,
            'idea_list' : idea_list,
    })

def devtool_delete(request, pk):
    devtool = get_object_or_404(DevTool, pk=pk)

    if request.method == "POST":
        devtool.delete()
        return redirect("blog:devtool_list")
    else:
        return redirect("blog:devtool_detail", pk=devtool.pk)


def devtool_new(request):
    if request.method == "POST":
        form = DevForm(request.POST, request.FILES)
        if form.is_valid():
            devtool = form.save()
            return redirect("blog:devtool_detail", pk=devtool.pk)
    else:
        form = DevForm()
        ctx = {
            "form": form
        }
        return render(request, "blog/devtool_create.html", ctx)

def devtool_update(request, pk):
    devtool = get_object_or_404(DevTool, pk=pk)

    if request.method == "POST":
        form = DevForm(request.POST, request.FILES, instance=devtool)
        if form.is_valid():
            devtool = form.save()
            return redirect("blog:devtool_detail", pk=devtool.pk)
    else:
        form = DevForm(instance=devtool)
        ctx = {
            "form": form
        }
        return render(request, "blog/devtool_update.html", ctx)
