
from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='user-detail',  # Replace with the actual view name
        lookup_field='pk'  # Specify the lookup field (e.g., 'pk' for primary key)
        )
    # id = serializers.IntegerField(read_only=True)
    class Meta:
        model = User
        # fields = '__all__'
        fields = ['url','id', 'username', 'email', 'groups']
        