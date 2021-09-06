from rest_framework import serializers
# products
from bills.models import Bills


class billserializers(serializers.ModelSerializer):

    class Meta:
        model=Bills
        fields=('id','bill_product','company_name')


        
        