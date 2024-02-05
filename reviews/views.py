from rest_framework import generics
from reviews.models import Review
from reviews.serializers import ReviewSerializer

class ReviewCreatelistView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
class ReviewRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

# Create your views here.
