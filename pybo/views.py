from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator

from .models import Question, Answer
from .forms import QuestionForm, AnswerForm


def index(request) : 
    ''' 기본 화면 '''
     # 입력 파라미터
    page = request.GET.get('page', '1')  # 페이지


    # 조회
    question_list = Question.objects.order_by('-create_date')


    # 페이징처리
    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {'question_list': page_obj}

    return render(request, 'pybo/question_list.html', context)


def detail(request, question_id) : 
    ''' pybo내용 출력 '''
    
    question = Question.objects.get(id = question_id)
    context = {'question' :  question }
    
    return render(request, 'pybo/question_detail.html', context)
    

def answer_create(request, question_id) : 
    ''' 답변등록 '''
    question = get_object_or_404(Question, pk=question_id)
    print(request.POST.get('content'))
    
    if request.method == 'POST' : 
        form = AnswerForm(request.POST) 
        if form.is_valid() : 
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            
            return redirect('pybo:detail', question_id=question_id)
        
    else : 
        form = AnswerForm()
    
    context = {'question':question, 'form':form }
    
    return render(request, 'pybo/question_detail.html', context)



def question_create(request) : 
    ''' 질문 등록하기 '''
    
    if request.method == 'POST' : 
        form = QuestionForm(request.POST) 
        if form.is_valid() : 
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect("pybo:index")
        
    else : 
        form = QuestionForm()
        
    context = {'form':form}
    
    return render(request, 'pybo/question_form.html', context)



