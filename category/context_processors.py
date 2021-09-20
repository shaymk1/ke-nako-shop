from .models import Category

#displaying categories from the navbar

def menu_links(request):
  links = Category.objects.all()
  return dict(links=links)