from rest_framework.generics import CreateAPIView, ListAPIView

from rest_framework.exceptions import ValidationError

from .serializers import UserDataSerializer
from .models import VerifiedUser


class RegisterUser(CreateAPIView):
    serializer_class = UserDataSerializer


class GetUserData(ListAPIView):
    serializer_class = UserDataSerializer

    def get_queryset(self):
        signature = self.request.data.get("signature", None)

        if signature is None:
            raise ValidationError("Signature is required")
        else:
            queryset = VerifiedUser.objects.filter(signature=signature)
            if not queryset.exists():
                raise ValidationError("Signature is invalid")
            return queryset
