from django.urls import path

from .views import index, kinesiologo_create, atencion, deportista_create, deportista_listar, kinesiologo_listar


urlpatterns = [path('', index),
                path('kinesiologo/kine', kinesiologo_create),
                path('kinesiologo/list/kine/', kinesiologo_listar),
                path('deportista/depor', deportista_create),
                path('Deportista/list/depor', deportista_listar),
                path('atencion/atencion', atencion), 
                                                      
]



