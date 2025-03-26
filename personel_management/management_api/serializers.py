from .models import Military, Diploma, Children
from  rest_framework import serializers


class DiplomaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diploma
        fields = '__all__'

class ChildrenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Children
        fields = '__all__'

class MilitarySerializer(serializers.ModelSerializer):
    children = ChildrenSerializer(many=True, read_only=True)
    diplomas = DiplomaSerializer(many=True, read_only=True)
    class Meta:
        model = Military
        fields = '__all__'

