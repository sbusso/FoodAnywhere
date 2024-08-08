from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema_view, OpenApiResponse, extend_schema
from orders.models import Order
from orders.serializers import OrderSerializer


@extend_schema_view(
    get=extend_schema(
        summary="List of a users orders",
        description="List all orders for",
        responses={
            200: OrderSerializer(many=True),
            403: OpenApiResponse(description="Unauthorized"),
        },
        tags=["Customer Orders"],
    ),
    post=extend_schema(
        summary="Create an order",
        description="Create an order for the user",
        responses={
            201: OrderSerializer(),
            400: OpenApiResponse(description="Bad Request"),
            403: OpenApiResponse(description="Unauthorized"),
        },
        tags=["Customer Orders"],
    ),
)
class OrderListCreateView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = OrderSerializer

    def get_queryset(self):
        return (
            Order.objects.select_related("restaurant", "user")
            .prefetch_related("items", "items__product")
            .filter(user=self.request.user)
            .order_by("-created_at")
        )

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["user"] = self.request.user
        return context
