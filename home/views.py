from django.shortcuts import render
# from django.http import HttpResonse, Http404
# Create your views here.
def home(request):
	content = {
	'name': 'Nick McCrory',
	'description': '19. Coder.',
	'fact': 'My favorite TV show is the Walking Dead',
	}
	return render(request, 'home/home.html', content)
