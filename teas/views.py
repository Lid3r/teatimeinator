from django.http import HttpRequest, JsonResponse
from django.shortcuts import get_object_or_404
from .models import Tea, TeaDescription, TeaCharacteristics, TeaUtils


def details(request: HttpRequest, tea_id: int):
    if request.method != 'GET':
        return JsonResponse({'errorInfo': 'method_not_allowed'}, status=405)

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
        return JsonResponse({'errorInfo': 'method_not_allowed'}, status=405)

    tea_types = request.GET.get('type', TeaUtils.all_choices)

    if type(tea_types) is str:
        tea_types = tea_types.split(',')

    search = request.GET.get('search', '')
    sort = request.GET.get('sort', 'id')

    return JsonResponse({'result': [tea.serialize() for tea in Tea.objects.filter(tea_type__in=tea_types, tea_name__icontains=search).order_by(sort)]}, status=200)
