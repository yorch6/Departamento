from django.conf.urls import url, include

from .views import DepartamentoList, DepartamentoCreate, DepartamentoUpdate, DepartamentoDelete

urlpatterns = [
    url(r'^listar$', DepartamentoList.as_view(), name='departamento_listar'),
    url(r'^nuevo$', DepartamentoCreate.as_view(), name='departamento_crear'),
    url(r'^editar/(?P<pk>\d+)/$', DepartamentoUpdate.as_view(), name='departamento_editar'),
    url(r'^eliminar/(?P<pk>\d+)/$', DepartamentoDelete.as_view(), name='departamento_eliminar'),

]



