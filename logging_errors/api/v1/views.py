from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status, generics
from rest_framework.response import Response

from .serializers import ErrorSerializer
from logging_errors.models import Error

from crashlytics.sdk import error_handler


class ErrorCreateView(generics.GenericAPIView):
    queryset = Error.objects.all()
    serializer_class = ErrorSerializer

    @error_handler
    def post(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            return Response({'details': 'Invalid application token.'}, status=status.HTTP_403_FORBIDDEN)
