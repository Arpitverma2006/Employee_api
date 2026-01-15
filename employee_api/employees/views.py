from rest_framework import viewsets
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.pagination import PageNumberPagination

class EmployeePagination(PageNumberPagination):
    page_size = 10

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    pagination_class = EmployeePagination

    def get_queryset(self):
        qs = super().get_queryset()
        department = self.request.query_params.get('department')
        role = self.request.query_params.get('role')

        if department:
            qs = qs.filter(department=department)
        if role:
            qs = qs.filter(role=role)
        return qs
