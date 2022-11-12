from django.contrib import admin

from .models import Categoria, Comanda, ItemCardapio, ItemPedido, Mesa

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Comanda)
admin.site.register(ItemCardapio)
admin.site.register(ItemPedido)
admin.site.register(Mesa)
