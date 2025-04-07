from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


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
    recomendations = models.TextField(("Recomendações"))
        
    author = models.ForeignKey(User, verbose_name=("Autor"), on_delete=models.CASCADE)
    category = models.ForeignKey(CategoryModel, verbose_name=("Categoria"), on_delete=models.CASCADE)
    

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("places:detail", kwargs={"pk": self.pk})
    

class Comment(models.Model):
    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    post = models.ForeignKey(PostModel, on_delete=models.CASCADE)
    message = models.CharField(("Mensagem") ,max_length=200)
    author = models.ForeignKey(User ,on_delete=models.CASCADE)
    created_at = models.DateField(("Comentado em") ,auto_now_add=True)

    def __str__(self):
        return f"Comentário de {self.author.username} no post '{self.post.title}'"