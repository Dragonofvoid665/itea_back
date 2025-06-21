from rest_framework import serializers
from .models import *
class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class Category_of_coursesSeriaizerdetial(serializers.ModelSerializer):
    course = CoursesSerializer(many=True,read_only=True)
    class Meta:
        model = Course_Category
        fields = '__all__'

class Category_of_coursesSerializerlist(serializers.ModelSerializer):
    class Meta:
        model = Course_Category
        fields = ['id','name','image']

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'

class VacanseSerializers(serializers.ModelSerializer):
    class Meta:
        model = Vacansy
        fields ='__all__'

class EmailSerializers(serializers.ModelSerializer):
    class Meta:
        model = News_email
        fields = '__all__'

class NewsSerializer(serializers.ModelSerializer):
    new_email = EmailSerializers(many=True,read_only=True)
    class Meta:
        model = News
        fields = '__all__'
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.places == 0:
            fields_to_exclude = ['new_email', 'places', 'ordered_places']
            for field in fields_to_exclude:
                representation.pop(field, None)
        return representation
    
