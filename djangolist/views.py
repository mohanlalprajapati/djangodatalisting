from django.shortcuts import render
from django.views.generic import ListView
from .models import Product
from .filters import ProductFilter
# Create your views here.

class FilteredListView(ListView):
    filterset_class = None

    def get_queryset(self):
        # Get the queryset however you usually would.  For example:
        queryset = super().get_queryset()
        # Then use the query parameters and the queryset to
        # instantiate a filterset and save it as an attribute
        # on the view instance for later.
        self.filterset = self.filterset_class(self.request.GET, queryset=queryset)
        # Return the filtered queryset
        return self.filterset.qs.distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Pass the filterset to the template - it provides the form.
        context['filterset'] = self.filterset
        return context

class ProductListView(FilteredListView):
    template_name = "djangolist/my_product_list.html"
    model = Product
    filterset_class = ProductFilter
    paginate_by = 10


class ProductListInfiniteView(FilteredListView):
    template_name = "djangolist/infinite_product_list.html"
    model = Product
    paginate_by = 3
    context_object_name = "products"
    filterset_class = ProductFilter