from rest_framework import serializers
from .models import Subscription

class SubscriptionsSerializer(serializers.ModelSerializer):
    client_name = serializers.CharField(source='client.company_name')
    # source='client.user.email' used to get the email from the user model
    email = serializers.CharField(source='client.user.email')

    class Meta:
        model = Subscription
        fields = ('id', 'plan_id', 'client_name', 'email')