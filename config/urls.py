from django.urls import path

from .views import index, kinesiologo_create, deportista_create, deportista_listar, kinesiologo_listar, atencion_create, tratamiento_listar


urlpatterns = [path('', index),
                path('kinesiologo/kine', kinesiologo_create),
                path('kinesiologo/list/kine/', kinesiologo_listar),
                path('deportista/depor', deportista_create),
                path('Deportista/list/depor', deportista_listar),
                path('atencion/atencion', atencion_create),
                path('historial/historial', tratamiento_listar),  

                                                      
]



