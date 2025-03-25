from .models import Military, Diploma, Children
from  rest_framework import serializers

class MilitarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Military
        fields = '__all__'

class DiplomaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diploma
        fields = '__all__'

class ChildrenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Children
        fields = '__all__'