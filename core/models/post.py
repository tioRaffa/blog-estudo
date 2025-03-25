from django.db import models
from django.contrib.auth.models import User

class CategoryModel(models.Model):
    name = models.CharField(("Nome"), max_length=50)
    
    def __str__(self):
        return self.name


class PostModel(models.Model):
    image = models.ImageField(("Foto"), upload_to='pulication_image/post/%y/%m/%d')
    title = models.CharField(("Titulo"), max_length=50)
    is_published = models.BooleanField(("Esta Publicado?"), default=False)
    created_at = models.DateField(("Criado"), auto_now_add=True)
    cost = models.TextField(("Custos"))
    description = models.TextField(("Descrição"))
    recommendations = models.TextField(("Recomendações"))
        
    author = models.ForeignKey(User, verbose_name=("Autor"), on_delete=models.CASCADE)
    category = models.ForeignKey(CategoryModel, verbose_name=("Categoria"), on_delete=models.CASCADE)
    

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
