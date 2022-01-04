from rest_framework import serializers
from . models  import Registration

class Serializer(serializers.ModelSerializer):
   class Meta:
       model = Registration
       fields = '__all__'