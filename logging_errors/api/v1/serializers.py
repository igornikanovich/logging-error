from rest_framework import serializers

from logging_errors.models import Error, Application


class ErrorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Error
        fields = ('type', 'date', 'message', 'stacktrace', )

    def create(self, validated_data):
        token = self.context.get('request').parser_context['kwargs']['token']
        validated_data['app'] = Application.objects.get(token=token)
        return Error.objects.create(**validated_data)
