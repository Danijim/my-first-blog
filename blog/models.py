from django.db import models
from django.utils import timezone

class Post(models.Model): 
    """
    define nuestro modelo (es un objeto)
    class: indica que definimos un objeto
    Post: es el nombre del modelo (comienza en mayuscula)
    models.Model: significa que Post es un modelo de Django, asi este lo guarda en la base
    """
    author = models.ForeignKey('auth.User') #vinculo con otro modelo
    title = models.CharField(max_length = 200) #texto con num limitado caracteres
    text = models.TextField() #textos largos sin limite de caracteres
    created_date = models.DateTimeField(default=timezone.now) #fecha y hora
    published_date = models.DateTimeField(blank=True, null=True) #fecha y hora
    def publish(self):
        """
        es el metodo publicar que mencionabamos
        def: significa que se trata de una funcion o metodo
        publish: nombre del metodo (comienza en minuscula)
        """
        self.published_date=timezone.now()
        self.save()
    def __str__(self):
        """
        Los metodos devuelven algo con return, este en concreto devuelve
        un string con un titulo de post
        """
        return self.title

# Create your models here.
