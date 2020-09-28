from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *

class UserDetailsSerializers(serializers.ModelSerializer):
	class Meta:
		model = UserDetails
		fields ='__all__'

class ExpensesSerializers(serializers.ModelSerializer):
	class Meta:
		model = Expenses
		fields ='__all__'

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']