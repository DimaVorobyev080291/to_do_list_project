from rest_framework import serializers
from to_do_list_app.models import To_do_list
from django.utils.timezone import localtime
from rest_framework.exceptions import ValidationError

today = localtime()


class To_do_listSerializer(serializers.ModelSerializer):
    """
    Serializer таблице To_do_list для представления To_do_list_ViewSet
    """
    class Meta:
        model = To_do_list
        fields = ['id', 'heading', 'description', 'term', 'status', 'created_at', 'updated_at']

    def validate(self, attrs):
        """
        Метод валидации срока выполнения , если срок меньше даты и времени создания то выдает ошибку
        """
        if attrs['term'] == None:
            return attrs
        elif attrs['term'] != None:
            if today > attrs['term']:
                raise ValidationError('Срок выполнения не верный ')
            return attrs
        
    
    def create(self, validated_data):
        """
        Переопределение метода create , проверям стутус выполнения при создание задачи 
        """
        if validated_data['status'] == 'Выполнено':
            raise ValidationError('Выбран не верный статус.')
        return super().create(validated_data)