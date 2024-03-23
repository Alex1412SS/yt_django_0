import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import Women

# class WomenModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content


class WomenSerial(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Women
        fields = "__all__"


    #title = serializers.CharField(max_length=255)
    # content = serializers.CharField()
    # time_cre = serializers.DateTimeField(read_only=True)
    # time_upd = serializers.DateTimeField(read_only=True)
    # is_pub = serializers.BooleanField(default=True)
    # cat_id = serializers.IntegerField()
    #
    # def create(self, validated_data):
    #     return Women.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get("title", instance.title)
    #     instance.content = validated_data.get("content", instance.content)
    #     instance.time_upd = validated_data.get("time_upd", instance.time_upd)
    #     instance.is_pub = validated_data.get("is_pub", instance.is_pub)
    #     instance.cat_id = validated_data.get("cat_id", instance.cat_id)
    #     instance.save()
    #     return instance
    #
    # def delete(self, validated_data):
    #     return Women.objects.delete(**validated_data)

# def encode():
#     model =  WomenModel('Hello niggaa', 'i am cool')
#     model_sr = WomenSerial(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)
#
# def decode():
#     stream = io.BytesIO(b'{"title":"Hello niggaa", "content":"i am cool"}')
#     data = JSONParser().parse(stream)
#     serializer = WomenSerial(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)