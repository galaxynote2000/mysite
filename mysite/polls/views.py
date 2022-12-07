from django.shortcuts import render, get_object_or_404
from .models import Question
from django.http import HttpResponse

def index(request):
    latest_question_list = Question.objects.order.by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
    'latest_question_list' : latest_question_list
    }
    return HttpResponse(template.render(context, request))
# Create your views here.
def detail(request, question_id):
    return render(request, 'polls/deatil.html', {'question': question})
    question = get_object_or_404(Question, pk = question_id)

def results(request, question_id):
    response = "your looking at the results of the question %s"
    reutrn HttpResponse(response %question_id)

def vote(request, question_id):
    reutrn HttpResponse("you are volting on question %s" %question_id)
