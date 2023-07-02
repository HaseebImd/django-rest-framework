from rest_framework import serializers
from .models import *


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        # fields = ['id','first_name','last_name','age','email','phone','address']
        # exclude = ['id']
        fields = "__all__"

    def validate(self, data):
        if data["age"] < 18:
            raise serializers.ValidationError({"error": "age must be greater than 18"})

        if data["first_name"] == data["last_name"]:
            raise serializers.ValidationError(
                {"error": "first name and last name must be different"}
            )

        if data["first_name"]:
            for i in data["first_name"]:
                if i.isdigit():
                    raise serializers.ValidationError(
                        {"error": "first name must not contain numbers"}
                    )

        return data


# Example of Nested Serializer

"""

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Book
        fields = '__all__'

"""
