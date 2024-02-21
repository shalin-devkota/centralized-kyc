from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework import status


@api_view(["POST"])
@permission_classes([IsAdminUser])
def check_bank(request):
    if request.user.role == "bank":
        return Response({"message": "You are a bank"}, status=status.HTTP_200_OK)
    else:
        return Response(
            {"message": "You are not a bank"}, status=status.HTTP_400_BAD_REQUEST
        )


# Create your views here.
