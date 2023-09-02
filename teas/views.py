from django.http import HttpRequest, JsonResponse
from django.shortcuts import get_object_or_404
from .models import Tea, TeaDescription, TeaCharacteristics


def details(request: HttpRequest, tea_id: int):
    if request.method != 'GET':
        return JsonResponse({'errorInfo': 'Method Not Allowed'}, status=405)

    foundTea = get_object_or_404(Tea, pk=tea_id)

    try:
        foundDetails = TeaDescription.objects.filter(tea_ref=tea_id)
        if len(foundDetails) == 0:
            raise TeaDescription.DoesNotExist
    except TeaDescription.DoesNotExist:
        return JsonResponse({'errorInfo': 'no_description'}, status=500)

    try:
        foundCharacteristics = TeaCharacteristics.objects.get(tea_ref=tea_id)
    except TeaCharacteristics.DoesNotExist:
        return JsonResponse({'errorInfo': 'no_characteristics'}, status=500)

    return JsonResponse(
        {'tea': foundTea.serialize(),
         'description': [detail.serialize() for detail in foundDetails],
         'characteristics': foundCharacteristics.serialize()
         }, status=200)


def filter(request: HttpRequest):
    if request.method != 'GET':
        return JsonResponse({'errorInfo': 'Method Not Allowed'}, status=405)

    tea_types = request.GET.getlist('type', [])
    search = request.GET.get('search', '')

    print(tea_types)
    print(search)

    if len(tea_types) == 0 and len(search) == 0:
        return JsonResponse([tea.serialize() for tea in Tea.objects.all()], safe=False)

    if len(tea_types) == 0:
        return JsonResponse([tea.serialize() for tea in Tea.objects.filter(tea_name__icontains=search)], safe=False)

    if len(search) == 0:
        return JsonResponse([tea.serialize() for tea in Tea.objects.filter(tea_type__in=tea_types)], safe=False)

    return JsonResponse([tea.serialize() for tea in Tea.objects.filter(tea_type__in=tea_types, tea_name__icontains=search)], safe=False)
