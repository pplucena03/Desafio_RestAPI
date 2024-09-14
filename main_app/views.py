from django.shortcuts import render, redirect
from .services import create_event
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class ApiView(APIView):
    def post(self, request):
        pass

    def get(self, request):
        pass