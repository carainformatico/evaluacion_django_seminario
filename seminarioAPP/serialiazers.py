from rest_framework import serializers
from seminarioAPP.models import seminario

class SeminarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = seminario
        fields = '__all__'