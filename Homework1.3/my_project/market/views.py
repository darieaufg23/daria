# market/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Product
from .forms import ProductForm

class ProductListView(ListView):
    model = Product
    template_name = 'market/product_list.html'
    context_object_name = 'products'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'market/product_detail.html'
    context_object_name = 'product'

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'market/product_form.html'

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'market/product_form.html'

class ProductDeleteView(DeleteView):
    model = Product
    success_url = '/products/'
    template_name = 'market/product_confirm_delete.html'
