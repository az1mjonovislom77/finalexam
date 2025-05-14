import django_filters
from .models import Product

class ProductFilter(django_filters.FilterSet):
    # Min va max narx orqali filtrlash
    price_min = django_filters.NumberFilter(field_name='price', lookup_expr='gte', label="Min Price")
    price_max = django_filters.NumberFilter(field_name='price', lookup_expr='lte', label="Max Price")

    # Kategoriya bo'yicha filtrlash
    category = django_filters.NumberFilter(field_name='category__id', label="Category")

    # Mahsulot nomi bo'yicha filtrlash
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains', label="Product Name")

    # Mahsulotning izohlaridan biror so'z bo'yicha filtrlash
    description = django_filters.CharFilter(field_name='description', lookup_expr='icontains', label="Description")

    # Mahsulotning yildan qaysi vaqtda chiqarilganini filtrlash
    created_after = django_filters.DateFilter(field_name='created_at', lookup_expr='gte', label="Created After")
    created_before = django_filters.DateFilter(field_name='created_at', lookup_expr='lte', label="Created Before")

    class Meta:
        model = Product
        fields = ['price_min', 'price_max', 'category', 'name', 'description', 'created_after', 'created_before']
