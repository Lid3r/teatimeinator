from django.http import HttpRequest, JsonResponse
from django.contrib.auth import authenticate, login
from rest_framework.authtoken.models import Token

from user.models import Fren
from django.contrib.auth.models import User

from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes, authentication_classes, api_view


@api_view(['GET'])
@authentication_classes([BasicAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_user_info(request: HttpRequest):
    if (request.method != 'GET'):
        return JsonResponse({'errorInfo': 'method_not_allowed'}, status=405)
    token_parts = str(request.META.get('HTTP_AUTHORIZATION', '')).split(' ')

    print(request.META.get('HTTP_AUTHORIZATION', ''))

    if len(token_parts) == 2 and token_parts[0].lower() == 'token':
        token_key = token_parts[1]

        try:
            token = Token.objects.get(
                key=token_key)
            user_name = token.user.username
            fren = User.objects.get(username=user_name)
            fren = Fren.objects.get(user=fren)
            """????"""
            return JsonResponse({"name": user_name, "isHost": fren.is_host})
        except Token.DoesNotExist:
            return JsonResponse({"errorInfo": "user_not_found"})


def login_user(request: HttpRequest):
    if (request.method != 'POST'):
        return JsonResponse({'errorInfo': 'method_not_allowed'}, status=405)

    user = authenticate(username=request.POST.get('user'),
                        password=request.POST.get('password'))

    if (user is not None):
        login(request, user)
    else:
        return JsonResponse()
