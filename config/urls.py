from django.urls import path

from .views import index, kinesiologo_create, deportista_create, deportista_listar, kinesiologo_listar, atencion_create, tratamiento_listar, depor_eliminar, kine_eliminar, estadistica, deportista_editar, kinesiologo_editar


urlpatterns = [path('', index),
                path('kinesiologo/kine', kinesiologo_create),
                path('kinesiologo/list/kine/', kinesiologo_listar),
                path('deportista/depor', deportista_create),
                path('Deportista/list/depor', deportista_listar),
                path('atencion/atencion', atencion_create),
                path('historial/historial', tratamiento_listar),
                path('deportista/<int:deportista_id>/delete', depor_eliminar), 
                path('kinesiologo/<int:kinesiologo_id>/delete', kine_eliminar), 
                path('deportista/<int:deportista_id>/editar', deportista_editar),
                path('kinesiologo/<int:kinesiologo_id>/editar', kinesiologo_editar),
                path('estadistica', estadistica),

]






