from django.http import HttpRequest, JsonResponse
from django.shortcuts import get_object_or_404
from .models import Meeting, TeaChoices, Tea, SerializedSelections

from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes, authentication_classes, api_view


def get_all(request: HttpRequest):
    if (request.method != 'GET'):
        return JsonResponse({'errorInfo': 'method_not_allowed'}, status=405)

    return JsonResponse([meeting.serialize() for meeting in Meeting.objects.all()], safe=False)


@api_view(['GET'])
@authentication_classes([BasicAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def details(request: HttpRequest, meeting_id: int):
    if (request.method != 'GET'):
        return JsonResponse({'errorInfo': 'method_not_allowed'}, status=405)

    found_meeting = get_object_or_404(Meeting, pk=meeting_id)

    try:
        found_tea_choices = TeaChoices.objects.filter(
            meeting_ref=found_meeting.pk)
        if (len(found_tea_choices) == 0):
            raise TeaChoices.DoesNotExist
    except TeaChoices.DoesNotExist:
        return JsonResponse(status=204)

    serialized_selections = SerializedSelections()

    people_in_meeting = found_tea_choices.values_list(
        'person', flat=True).distinct()

    for person_in_meeting in people_in_meeting:
        tea_refs = found_tea_choices.filter(
            person=person_in_meeting).values_list('tea_ref', flat=True).distinct()

        teas = [tea.serialize() for tea in Tea.objects.filter(pk__in=tea_refs)]
        serialized_selections.merge_choices(person_in_meeting, teas)

    return JsonResponse({
        'id': found_meeting.pk,
        'date': found_meeting.date,
        'title': found_meeting.title,
        'personalSelections': serialized_selections.get_selections()
    })


@api_view(['GET'])
@authentication_classes([BasicAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def add_to_meeting(request: HttpRequest):
    if (request.method != 'POST'):
        return JsonResponse({'errorInfo': 'method_not_allowed'}, status=405)

    POST_data = request.POST

    meeting_id = POST_data.get('meetingId')
    person = POST_data.get('person')
    tea_ids = POST_data.getlist('teas')

    found_meeting = get_object_or_404(Meeting, pk=meeting_id)

    for id in tea_ids:
        found_tea = Tea.objects.get(pk=id)

        TeaChoices(meeting_ref=found_meeting,
                   person=person, tea_ref=found_tea).save()
