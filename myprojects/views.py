from django.shortcuts import render, redirect
from .models import Project,Review
from .forms import ProjectForm, ReviewForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


# Create your views here.


def projects(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    projects = Project.objects.distinct().filter(Q(title__icontains = search_query) | Q(tags__name__icontains = search_query))

    page = request.GET.get('page')
    result = 3

    paginator = Paginator(projects,result)
    
    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        projects = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        projects = paginator.page(page)

    total_page = range(paginator.num_pages)

    data = {
        'projects' : projects,
        'search':search_query, 
        'total_page':total_page
    }
    return render(request, 'myprojects/projects.html', data)


def project(request, pk):
    project = Project.objects.get(id = pk) 
    tags = project.tags.all()
    reviews = project.review_set.all()
    form = ReviewForm()
    print(form)
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.owner = request.user.profile
            review.project = project
            review.save()
            project.getVoteCount
 
    data = {
        'project' : project, 
        'tags' : tags, 
        'reviews' : reviews,
        'form':form
        }
    
    return render(request, 'myprojects/single_project.html',data) 


@login_required(login_url='login')
def project_form(request):
    profile = request.user.profile
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            return redirect(request.GET['next'] if 'next' in request.GET else 'projects')
    data = {
        'form' : form
    }
    return render(request, 'myprojects/project_form.html', data)


@login_required(login_url='login')
def update_project(request,pk):
    # this is for only login user can only update its own profile other can not modify its by urls
    projects = request.user.profile
    project = projects.project_set.get(id = pk)

    
    form = ProjectForm(instance=project)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect(request.GET['next'] if 'next' in request.GET else'projects')
    data = {
        'form' : form
    }
    return render(request, 'myprojects/project_form.html', data)

@login_required(login_url='login')
def  delete_project(request, pk):
    project = Project.objects.get(id = pk)
    if request.method == 'POST':
        project.delete()
        print(request.GET)
        return redirect(request.GET['next'] if 'next' in request.GET else 'projects')
    data = {
        'project' : project
    }
    return render(request, 'myprojects/delete_project.html',{'project':project})