from django.http import HttpResponse, Http404
from django.shortcuts import render # inserted this line
def index(request):
  context = {
    'questions': [
      { 'id': 1, 'content': 'Why is there a light in the fridge and not in the freezer?'},
      { 'id': 2, 'content': 'Why don\'t sheep shrink when it rains?'},
      { 'id': 3, 'content': 'Why are they called apartments when they are all stuck together?'},
      { 'id': 4, 'content': 'Why are cigarettes sold at gas stations where smoking is prohibited?'},
    ]
  }
  return render(request, 'quiz/index.html', context)
def show(request, question_id):
  if int(question_id) == 1:
    return HttpResponse('<h1>Page found!</h1>')
  else:
    raise Http404