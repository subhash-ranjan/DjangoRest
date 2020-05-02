from WebApp.models import Employee
from rest_framework import viewsets, permissions
from .serializers import WebAppSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    permission_classes = [
        permissions.AllowAny,
    ]
    serializer_class = WebAppSerializer

    # permission_classes = [
    #     permissions.IsAuthenticated,
    # ]
    # serializer_class = WebAppSerializer

    # def get_queryset(self):
    #     return self.request.user.users.all()

    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)