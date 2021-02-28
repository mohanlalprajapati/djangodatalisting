import django_filters
from .models import Product


class ProductFilter(django_filters.FilterSet):
    
    def __init__(self, data, *args, **kwargs):
        data = data.copy()
        data.setdefault('format', 'paperback')
        data.setdefault('order', '-added')
        super().__init__(data, *args, **kwargs)

    class Meta:
        model = Product
        fields = {'name':['icontains'],'category':['exact']}
       
