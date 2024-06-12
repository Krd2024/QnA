from django.contrib import admin
from main import models
import inspect

for name, obj in inspect.getmembers(models):
    if inspect.isclass(obj):
        try:
            admin.site.register(obj)
        except:
            ...
