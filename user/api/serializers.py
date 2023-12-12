from rest_framework import serializers
from user.models import Fren


class userSerializers(serializers.ModelSerializer):

    class Meta:
        model = Fren
        fields = '__all__'
