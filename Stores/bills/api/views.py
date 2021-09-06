from rest_framework import viewsets


# models
from bills.models import Bills
from bills.api.serializers import billserializers

# permisos
from  bills.api.permission import UserToUser


class BillsViewset(viewsets.ModelViewSet):
    serializer_class = billserializers
    permission_classes=[UserToUser]

    def get_queryset(self):
        return Bills.objects.filter(client_id=self.request.user,state=False)

    def perform_create(self, serializer):
        serializer.save(client_id=self.request.user)



