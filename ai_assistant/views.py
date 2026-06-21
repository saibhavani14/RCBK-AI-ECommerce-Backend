from django.shortcuts import render

# Create your views here.
import os
from dotenv import load_dotenv
from google import genai

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
import os
from dotenv import load_dotenv
from google import genai


load_dotenv()
print("Gemini Key:", os.getenv("GEMINI_API_KEY"))
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

class AISearchView(APIView):

    permission_classes = [AllowAny]
    authentication_classes = []

    def post(self, request):

        prompt = request.data.get("prompt")

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return Response({
            "answer": response.text
        })