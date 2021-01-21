from django.shortcuts import render
from django.http import HttpResponse
from .models import Questions
# Create your views here.
def index(request):
    latest_questions = Questions.objects.order_by('pub_date')[:5]
    return render(request, "polls/index.html", {'latest_question':latest_questions})

def detail(request,question_id):
    return HttpResponse("This is detail view of the Questions %s" % question_id)

def result(request,question_id):
    return HttpResponse("This is Result of the question %s" % question_id)

def vote(request,question_id):
    return HttpResponse("This is vote of the question %s" % question_id)
