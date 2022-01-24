from rest_framework import serializers
from leads.models import Lead


# Lead Model Serializer
class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = ('id', 'name', 'email', 'message', 'created_at')



