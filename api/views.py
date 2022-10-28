from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.


class HomeView(APIView):
    def get(self, request):
        response = {"slackUsername": "matstick", "backend": True,
                    "age": 25, "bio": "I love backend development"}
        return Response(response)
