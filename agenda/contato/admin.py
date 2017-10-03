from django.contrib import admin
from agenda.contato.models import Contato


class ContatoAdmin(admin.ModelAdmin):
	list_display = ('contato_nome', 'contato_email', 'contato_telefone', 'contato_favorito')
	list_filter = ('contato_sexo', 'contato_favorito')
	search_fields = ['contato_nome']
	save_on_top = True
admin.site.register(Contato, ContatoAdmin)



