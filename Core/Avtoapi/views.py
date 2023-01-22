from rest_framework.viewsets import ModelViewSet
from .serializers import  SaleSerializer, UserSerializer, NewsSerializer
from .models import News, Sale, User
from rest_framework.generics import ListAPIView
from rest_framework.decorators import action
from rest_framework.response import Response
import django_filters.rest_framework
from django.db.models import Q

class AdvertsViewSet(ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

class CustomerViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class GetUserView(ListAPIView):
    queryset = User.objects.filter(Q(amount__gt=3))
    serializer_class = UserSerializer

class ProductViewSet(ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer

class GetProductView(ListAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['title']

class PostDelGetNews(ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    @action(methods=['Delete'], detail=True, url_path='delete')
    def delNews(self,request, pk=None):
        movie=self.queryset.get(id=pk)
        movie.delete()
        return Response('Объявление была удалена')
    @action(methods=['Post'], detail=False, url_path='post')
    def posNews(self,request, pk=None):
        title=self.queryset.create(name=request.data.get('title'))
        title.save()
        return Response('Объявление была создана')
    @action(methods=['GET'], detail=False,
            url_path='newsget')
    def news(self, request):
        news = request.news
        data = NewsSerializer(news).data
        return Response(data)


