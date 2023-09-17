# Django-React
## Setup
### Start a project
`django-admin startproject first_project`
Creation of new application api -> need to add it into project.settings -> INSTALLED APP
`django-admin startapp api`

Creation of new urls.py in the new app in order to let it manage the views

In project.urls use   `path('', include('api.urls'))`   in order to redirect the manage of path starting with '' to api.urls
```
from django.urls import path
from .views import main

urlpatterns = [
    path('', main)      # calling a view (main)
]

```

each time a module or database (models) has been modified
```
python manage.py makemigrations 
python manage.py migrate
```


### To run the project on localhost
`python manage.py runserver ``

## Django REST
### Models
Classes of the models should be created in api.models 
They should be superclasses of django.db.models.Model
```
from django.db import models
class Class_name(models.Model):
    attribute = models.CharField(max_length = ..., default = ..., unique = ...)
                models.BooleanField(...)
                models.DateTimeField(auto_now_add=True)
```
### Serializers
Allow to transform Django Objects into other format as jason...
```
from rest_framework import serializers
from .models import ModelClass

class ModelClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelClass
        fields = ('id', 'code', 'host', ...)    # Exactly the same fields of the model (id is automatically created)
```