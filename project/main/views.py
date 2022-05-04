from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions

from main.serializers import UserSerializer
from .tasks import supper_sum


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


def index(request):
    supper_sum.delay(5, 7)
    return HttpResponse("Hello, world. This is a simple stub.")
