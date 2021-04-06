Local ortamda kurulum için default veri tabanı sql
if you use replit, look at .replit file int root folder
if you get DisallowedHost change settings.py 

# Start
python3 -m virtualenv env
source env/bin/activate
python --version


django-admin startproject **projectname**
python manage.py startapp **apiname**


## Connect main project
- add installed app in settings py 
 ```
INSTALLED_APPS = [
  'rest_framework',
  'projectname.apps.apiname',
]
 ```

- create urls.py into **apiname** folder
- add below code into url.py file **projectname** folder
 ```
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('productapi.urls')),
]
 ```

- add below code into model.py apiname folder 
 ```
class Brand(models.Model):
    name = models.CharField(max_length=120)
    desc = models.CharField(max_length=2400)
    class Meta:
        db_table = 'brand'
 ```

- python manage.py makemigrations **apiname**
- python manage.py migrate
  - if you get any error, delete urls row from **projectname** folder
- add serialize file into **apiname**
  ```
from rest_framework import serializers
from productapi.models import  Brand
class BrandSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=120)

    def create(self, validated_data):
        return Brand.objects.create(**validated_data)
  ```
- change to urls.py that in **apiname**
  ```
from django.urls import path
from productapi.views import  BrandList, ProductList
urlpatterns = [
    path('brands/', BrandList.as_view()),
    path('products/', ProductList.as_view()),
]
  ```

- last step for basic start rest_framework. You need to add below code into views for you hive any response to enduser.
  ```
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from productapi.models import Brand
from productapi.serializers import BrandSerializer
class BrandList(APIView):
    def get(self, request, format=None):
        libraries = Brand.objects.all()
        serializer = BrandSerializer(libraries, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = BrandSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  ```

- open 
  - https://rest.misaliperver.repl.co/api/brands/
  ```
    {
      "name":"LCwaikiki"
    }
  ```
  - https://rest.misaliperver.repl.co/api/products/
  ```
    {
      "title": "Et kesme bıçağı",
      "price": 129.99,
      "imgSrc": "https://........."

    }
  ```





# Change Serializer
### oldcode
```
class BrandSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    def create(self, validated_data):
        return Brand.objects.create(**validated_data)
```
### newcode
```
class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ('id','name')
        #fields = '__all__'
```