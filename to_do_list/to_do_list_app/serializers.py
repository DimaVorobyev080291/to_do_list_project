from rest_framework import serializers
from to_do_list_app.models import To_do_list

class To_do_listSerializer(serializers.ModelSerializer):
    """
    Serializer таблице To_do_list для представления MeasurementCreateView
    """
    class Meta:
        model = To_do_list
        fields = ['id', 'heading', 'description', 'term', 'status', 'created_at', 'updated_at']