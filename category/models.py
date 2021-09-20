from django.db import models
from django.urls import reverse


class Category(models.Model):

    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, blank=True, unique=True)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('products_by_category', args=[self.slug])

    # def get_absolute_url(self):
    #     return reverse("products_by_category", kwargs={"pk": self.pk})
    # def get_absolute_url(self):
    #     return reverse('post-detail', kwargs={'category_slug': self.category_slug})

   

    # def get_absolute_url(self):
    #   return reverse('url name', args = [str(self.id)])
