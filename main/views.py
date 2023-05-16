from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Bilety, Chapter
from django.views import generic

def index(request):
    return render(request, 'main/index.html')

def rules(request):
    return render(request, 'main/rules.html')

def signs(request):
    return render(request, 'main/signs.html')

class BiletyView(generic.ListView):
    template_name = 'main/ticket_example.html'
    context_object_name = 'question_list'

    def get_queryset(self):
        """Return the questions. Bilety.objects.order_by('question_number')"""
        return Bilety.objects.filter(ticket_number__exact=1).order_by('question_number')


class DetailView(generic.DetailView):
    model = Bilety
    template_name = 'main/detail.html'


from django.core.paginator import Paginator
import random
score=0

def test_start(request):
    ticket= random.randint(1,5)
    return redirect(f'test/{ticket}')


def test(request, ticket):
    q = Bilety.objects.filter(ticket_number__exact=ticket).order_by('question_number')
    paginator = Paginator(q,1)
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)
    global score
    if page_num==None: score=0

    if page_num==20:
        context={'page_obj':page_obj,"finish":"true"}
    else:
        context ={'page_obj':page_obj}

    if request.method=="POST":
        answer=request.POST.get("answer")
        answer=answer.split(',')
        context['give_answer']=answer[0]
        context['correct']=answer[1]
        if answer[1]=='True':
            score+=1
    context['score']=score
    return render(request,'main/test.html',context)

def test_exam(request):
    ticket = random.randint(1, 5)
    return redirect(f'exam/{ticket}')

def exam(request, ticket):
    q = Bilety.objects.filter(ticket_number__exact=ticket).order_by('question_number')
    paginator = Paginator(q,1)
    page_num = request.GET.get('page')
    finish = request.GET.get('finish')
    page_obj = paginator.get_page(page_num)
    global score
    if finish:
        context={'score': score}
        return render(request,"main/exam_result.html", context)
    if page_num==None:
        score=0
    context ={'page_obj':page_obj}

    if request.method=="POST":
        answer=request.POST.get("answer")
        answer = answer.split(',')
        context['give_answer'] = answer[0]
        context['correct'] = answer[1]
        if answer[1]=='True':
            score+=1

    context['score']=score
    return render(request,'main/exam_test.html',context)

