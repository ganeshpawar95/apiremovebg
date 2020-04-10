from rest_framework import serializers
from  .models import Removebg


# Serializers define the API representation.
class RemovebgSerializer(serializers.ModelSerializer):
    class Meta:
        model = Removebg
        fields = ['id','images']




class RemovebgUpdateSerializer(serializers.ModelSerializer):
	
	class Meta:
		 model = Removebg
		 fields = ['id','images']


class RemovebgPostSerializer(serializers.ModelSerializer):
  
	class Meta:
		model = Removebg
		fields = '__all__'




