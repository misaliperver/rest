from rest_framework import serializers
from productapi.models import  Brand, Product
"""
class BrandSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=120)

    def create(self, validated_data):
        return Brand.objects.create(**validated_data)

class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=120)
    imageSrc = serializers.CharField(max_length=400)
    price = serializers.FloatField()

    def create(self, validated_data):
        return Product.objects.create(**validated_data)
"""
class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ('id','name','desc')
        #fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


