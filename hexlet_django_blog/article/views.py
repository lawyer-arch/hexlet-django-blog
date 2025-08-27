from django.shortcuts import render

TEAM = [
    {'name': 'Yoda', 'position': 'CEO'},
    {'name': 'Obi-Wan Kenobi', 'position': 'Senior Developer'},
    {'name': 'Anakin Skywalker', 'position': 'Junior Developer'},
    {'name': 'Jar Jar Binks', 'position': 'Trainee'},
]

def index(request):
    return render(request, "article/index.html", context={'TEAM': TEAM})
