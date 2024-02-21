from rest_framework.decorators import api_view

from rest_framework.response import Response


@api_view(["GET"])
def is_loggedin(request):
    if request.user.is_authenticated:
        return Response({"status": "ok :D "})
    return Response({"status": "not ok :()"})
