from rest_framework import serializers
from accounts.models import Costumer
from django.contrib.auth import get_user_model

#serializer do campo de endereço
class CostumerSerializer(serializers.ModelSerializer):

    address = serializers.CharField(max_length = 30)

    class Meta:
        model = Costumer
        fields = ('address',)

#serializer do usuário
class RegistrationSerializer(serializers.HyperlinkedModelSerializer):

    password = serializers.CharField(style = {'input_type':'password'}, write_only = True)
    costumer = CostumerSerializer();

    class Meta:
        model = get_user_model()
        fields = ('username', 'first_name', 'last_name', 'email', 'password', 'costumer')

    #função de criar usuário
    def create(self, validated_data):

        profile_data = validated_data.pop('costumer')

        user = get_user_model().objects.create(
            username = validated_data['username'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            email = validated_data['email'],
        )

        user.set_password(validated_data['password'])
        user.save()

        costumer = Costumer.objects.create(
            user = user,
            **profile_data
        )

        costumer.save()

        return user
