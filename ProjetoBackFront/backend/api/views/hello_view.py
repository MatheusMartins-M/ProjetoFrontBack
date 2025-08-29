from rest_framework.views import APIView
from rest_framework.response import Response
from django.views import View
from django.views.generic import DeleteView, CreateView, UpdateView, DetailView
from django.shortcuts import render, get_object_or_404, redirect
from api.forms.produto import ProdutoForm
from api.models.produto import Produto
from django.urls import reverse_lazy

class HelloView(APIView):
    def get(self, request):
        return Response({"message": "Olá do Django REST Framework!"})
    
class CreateViewClass(View):
    model = Produto
    form_class = ProdutoForm
    template_name = "exemplo/create.html"
    success_url = reverse_lazy('aula:exemplo_class_list')
    permission_required = 'aula.add_exemplo'
    raise_exception = True