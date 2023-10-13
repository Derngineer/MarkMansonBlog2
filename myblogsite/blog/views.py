from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Article,Comment
from django.template import loader
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout 
from django.contrib import messages
from .forms import SignUpForm,CommentForm
from django.core.exceptions import ValidationError


# Create your views here.




def sign_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']
        user = authenticate(request,username =username,password=password)

        try:
            user = authenticate(request, username=username, password=password)
        except ValueError:
            messages.error(request, ('Invalid username or password.'))
            return redirect('sign_in')
        except ValidationError:
            messages.error(request, ('Incorrect username or password.'))
            return redirect('sign_in')

        if user is not None:
            login(request, user)
            return redirect('main')

        else:
            print('this did not work out')
            messages.error(request, 'The credentials were invalid. Please try again.')
            return redirect('sign_in')


    print('this did not work out too')


    context = {

    }
    
    return render(request, 'blog/login.html',context)

def registration(request):
    
    if request.method == 'POST':

        form = SignUpForm(request.POST)

        if form.is_valid():

            form.save()
            return redirect('sign_in')

        else:
            print('form is not valid')
    else:
        print('METHOD NOT READ')
        form = SignUpForm()


    

    template = loader.get_template('blog/register.html')
    context ={
    'form': form,
    }

    return HttpResponse(template.render(context,request))

def index(request):
    my_articles = Article.objects.all().values()
    template = loader.get_template('blog/index.html')
    context={
        'my_articles':my_articles,
    }
   
    return HttpResponse(template.render(context,request))

def details(request,id):
    my_articles = Article.objects.get(id=id)
    comments = my_articles.comments.all()
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data = request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit = False)
            new_comment.my_articles = my_articles
            new_comment.save()
    else:
        comment_form = CommentForm()

    template = loader.get_template("blog/details.html")
    context ={
        "my_articles": my_articles,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form,


    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('blog/main.html')
    return HttpResponse(template.render())

def test(request):
    template = loader.get_template('blog/test.html')
    context ={
        'fruits': ['apple','banana','oranges'],
    }
    return HttpResponse(template.render(context,request))

def about_us(request):
    template = loader.get_template('blog/about.html')
    return HttpResponse(template.render())
    

