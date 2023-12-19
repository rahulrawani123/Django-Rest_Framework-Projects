from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'
        
    
def update(self,instance,validated_data):
    instance.id=validated_data.get('id',instance.id)
    instance.name=validated_data.get('name',instance.name)
    instance.roll=validated_data.get('roll',instance.roll)
    instance.city=validated_data.get('city',instance.city)    
    instance.save()
    return instance
