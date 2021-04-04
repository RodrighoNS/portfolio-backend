from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from .models import Apo
from .serializers import PostSerializer


class ApoViewSet(ModelViewSet):
    queryset = Apo.objects.all()
    serializer_class = ApoSerializer
    permission_classes = [AllowAny]
