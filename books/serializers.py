from django.forms import widgets 
from rest_framework import serializers 
from books.models import Books

class BooksSerializer(serializers.ModelSerializer):     
	class Meta:         
		model = Books         
		fields = ('title', 'author', 'pdate', 'pname', 'price', 'sum', 'url', 'img')
