from rest_framework.views import APIView
from .serializers import bookingSerializer, menuSerializer, UserSerializer
from .models import Booking, Menu
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework import status, generics
from django.contrib.auth.models import User


def index(request):
    return render(request, 'index.html', {})


class bookingView(APIView):
    def get(self, request):
        items = Booking.objects.all()
        serializer = bookingSerializer(items, many=True)
        return Response(serializer.data)


class menuView(APIView):
    def post(self, request):
        serializer = menuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(
            users, many=True, context={'request': request})
        return Response(serializer.data)


class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
