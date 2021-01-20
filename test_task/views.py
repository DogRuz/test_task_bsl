from django.forms import model_to_dict
from rest_framework.response import Response
from test_task.models import Person
from rest_framework import status
from rest_framework.decorators import api_view

from test_task.utils import validate_values, check_id_person


@api_view(['GET'])
def get_status(request):
    """
    Check server status
    :param request:
    :return status_code:
    """
    return Response('The server is running', status=status.HTTP_200_OK)


@api_view(['POST'])
def add_balance(request):
    """
    Card replenishment
    :param request:
    :return:
    """
    try:
        params = validate_values(request.POST)
    except ValueError as ex:
        return Response(
            dict(status=status.HTTP_400_BAD_REQUEST, result=False, addition={}, description=dict(errors_msg=str(ex))),
            status=status.HTTP_400_BAD_REQUEST)
    try:
        user = Person.objects.get(pk=params['id_person'])
        user.balance += params['sum']
        user.save()
        return Response(dict(status=status.HTTP_200_OK, result=True, addition=model_to_dict(user), description={}),
                        status=status.HTTP_200_OK)
    except Person.DoesNotExist:
        return Response(dict(status=status.HTTP_404_NOT_FOUND, result=False, addition={},
                             description=dict(errors_msg='No content')), status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def subtraction_balance(request):
    """
    Decrease in balance
    Balance replenishment
    :param request:
    :return:
    """
    try:
        params = validate_values(request.POST)
    except ValueError as ex:
        return Response(
            dict(status=status.HTTP_400_BAD_REQUEST, result=False, addition={}, description=dict(errors_msg=str(ex))),
            status=status.HTTP_400_BAD_REQUEST)
    try:
        user = Person.objects.get(pk=params['id_person'])
        possible = True if user.balance >= user.hold + params['sum'] else False
        print(possible)
        user.balance -= params['sum'] if possible else 0
        user.hold += params['sum'] if possible else 0
        user.save()
        if possible:
            return Response(
                dict(status=status.HTTP_200_OK, result=possible, addition=model_to_dict(user), description={}),
                status=status.HTTP_200_OK)
        else:
            return Response(
                dict(status=status.HTTP_402_PAYMENT_REQUIRED, result=possible, addition=model_to_dict(user),
                     description=dict(errors_msg='No cash')), status.HTTP_402_PAYMENT_REQUIRED)
    except Person.DoesNotExist:
        return Response(dict(status=status.HTTP_404_NOT_FOUND, result=False, addition={},
                             description=dict(errors_msg='No content')), status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_info_person(request):
    """
    Get info persona
    :param request:
    :return:
    """
    id_person = check_id_person(request.GET.get('id', None))
    if id_person is not None:
        try:
            user = Person.objects.get(pk=id_person)
            return Response(
                dict(status=status.HTTP_200_OK, result=True, addition=model_to_dict(user), description={}))
        except Person.DoesNotExist:
            return Response(dict(status=status.HTTP_404_NOT_FOUND, result=False, addition={},
                                 description=dict(errors_msg='No content')), status=status.HTTP_404_NOT_FOUND)
    else:
        return Response(
            dict(status=status.HTTP_400_BAD_REQUEST, result=False, addition={},
                 description=dict(errors_msg='Invalid parameters')), status=status.HTTP_400_BAD_REQUEST)
