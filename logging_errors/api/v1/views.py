from rest_framework import status, generics
from rest_framework.response import Response

from .serializers import ErrorSerializer
from logging_errors.models import Error


class ErrorCreateView(generics.GenericAPIView):
    queryset = Error.objects.all()
    serializer_class = ErrorSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
