from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework import routers, serializers, viewsets

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Artist(models.Model):
    name = models.CharField(max_length=100)
    work = models.ManyToManyField('Work')

class Work(models.Model):
    link = models.URLField()
    work_type = models.CharField(max_length=100)
    WORK_TYPE_CHOICES = [
        ('youtube', 'Youtube'),
        ('instagram', 'Instagram'),
        ('other', 'Other'),
    ]

# Serializers define the API representation.
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'name', 'user']

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['id', 'name', 'work']

class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = ['id', 'link', 'work_type']

# ViewSets define the view behavior.
class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class WorkViewSet(viewsets.ModelViewSet):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer

# Routers provide a way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'artists', ArtistViewSet)
router.register(r'works', WorkViewSet)

class UserRegistration(viewsets.ViewSet):
    serializer_class = UserSerializer

    def create(self, request):
        user = User.objects.create_user(
            username=request.data.get('username'),
            password=request.data.get('password'),
        )
        client = Client.objects.create(user=user, name=user.username)
        return Response({'message': 'User created successfully'})

@receiver(post_save, sender=User)
def create_client(sender, instance, created, **kwargs):
    if created:
        Client.objects.create(user=instance, name=instance.username)
