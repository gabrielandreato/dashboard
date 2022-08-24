from django.contrib import admin

# Register your models here.
from minha_dashboard.models import Vendas, Vendedor, Produto, Despesas

admin.site.register(Produto)
admin.site.register(Vendedor)
admin.site.register(Vendas)
admin.site.register(Despesas)
