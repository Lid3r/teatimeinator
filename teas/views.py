from django.http import JsonResponse

from .models import Tea


def index(request):
    return JsonResponse({'test': 'Henlo it is tea time :D'})


def details(request, tea_id):
    black = list(Tea.objects.filter(tea_type='BLACK'))
    return JsonResponse({'test': 'Henlo it is temst :D %s' % black[0]})
