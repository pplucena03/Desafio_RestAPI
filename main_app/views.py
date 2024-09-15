from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import EventSerializer
from .models import Event
from .filters import EventFilter
from .services import create_event

class EventApiView(APIView):
    def post(self, request):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        filterset = EventFilter(request.GET, queryset=Event.objects.all())
        serializer = EventSerializer(filterset.qs, many=True)
        return Response(serializer.data)
