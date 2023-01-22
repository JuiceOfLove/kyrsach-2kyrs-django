from rest_framework import serializers
from .models import User, Sale, News

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'



class SaleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sale
        fields = '__all__'

class NewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = News
        fields = '__all__'
