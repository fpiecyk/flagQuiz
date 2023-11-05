from django.shortcuts import render, redirect
from .models import FlagData, ResultsData
from .utils_temp import AnswerVariants
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required




# Create your views here.

def index(request):
     return render(request, "index.html")

   
def list_answers(request):
    answer_variants = AnswerVariants()
    correct_answer = answer_variants.correct_answer_add()
    all_variants = answer_variants.prompt_answer_add()
    user_score = request.session.get('user_score', 0)
    answered_questions = request.session.get('answered_questions', 0)
    message = None     
    
    if request.method == 'POST':            
        selected_answer = request.POST.get('selected_answer')
        correct_answer_form = request.POST.get('correct_answer')

        if selected_answer == correct_answer_form:
            user_score += 1
            message = f"Good answer! You gained 1 point. Your result is: {user_score}."
        else:
            message = f"Wrong answer! Your result is: {user_score}."    

        answered_questions += 1
        request.session['answered_questions'] = answered_questions
        request.session['user_score'] = user_score
    return render(request, 'home.html', {
                        'correct_answer': correct_answer, 
                        'all_variants': all_variants, 
                        'message': message,
                        'user_score': user_score,
                        'answered_questions': answered_questions + 1})


@login_required 
def user_result(request):
        result = request.session.get('user_score')
        results_data = ResultsData(player=request.user, player_score=result)
        results_data.save()
        
        del request.session['user_score']
        del request.session['answered_questions']
        return render(request, 'final_score.html', {'results_data': results_data})


@login_required 
def list_of_results(request):
     queryset = ResultsData.objects.all().order_by('-player_score',)    
     return render(request, 'results.html', {'queryset': queryset})

def register(request):
    if request.method == 'GET':
        return render(request, "register.html", {'user_form': RegisterForm()})
    else:
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 == password2:
                username_taken = User.objects.filter(username=username).exists()

                if username_taken:
                        error = 'This username is taken. Try again!'
                if not username_taken:
                    try:
                        validate_password(password1)
                    
                    except ValidationError as e:
                        return render(request, "register.html", {'password_errors':e.messages, 'user_form': RegisterForm()})

                    else:  
                        user = User.objects.create_user(
                            username=username, password=password1)
                        return redirect('login_user')

def login_user(request):
    if request.method == 'GET':
        return render(request, "login_page.html", {'form': AuthenticationForm()})
    else:
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            user_exists = User.objects.filter(username=username).exists()
            if user_exists:
                error = ' Incorrect password.'
            else:
                error = f'User with username {username} does not exist.'
            return render(request, 'login_page.html', {'form': AuthenticationForm(), 'error':error})
        
@login_required 
def logout_user(request):
    logout(request)
    return render(request, 'logout_page.html')