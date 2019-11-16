from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions, filters
from .models import Bill
from .serializers import BillSerializer


class BillView(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAdminUser,
    ]
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['id', 'amount', 'intake', 'digital', 'paid', 'date_order', 'date_paid', 'ordered_by_id',
                        'project_id', 'seller_id', ]
    search_fields = ['id', 'amount', 'intake', 'digital', 'paid', 'date_order', 'date_paid', 'ordered_by_id',
                     'project_id', 'seller_id', ]

    def get_queryset(self):
        return self.queryset.order_by('id')

    def perform_create(self, serializer):
        serializer.save(lead=self.request.user)
