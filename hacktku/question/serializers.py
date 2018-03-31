from rest_framework import serializers
from .models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        # fields = '__all__'
        fields = ('id', 'score')

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id','first_name','last_name','birthday','phone','address','coler','fruit','num','constellation','gender','blood','education')