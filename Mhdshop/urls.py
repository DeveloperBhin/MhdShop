from django.urls import path
from . import views 

urlpatterns = [
    path('',views.index,name='index'),
    path('Carpet_tiles/',views.Carpet_tiles,name='Carpet_tiles'),
    path('Interior_decoration/',views.Interior_decoration,name='Interior_decoration'),
    path('furniture/',views.furniture,name='furniture'),
    path('spc/',views.spc,name='spc'),
    path('Lvt/',views.Lvt,name='Lvt'),
    path('Vinylsheetfloor/',views.Vinylsheetfloor,name='Vinylsheetfloor'),
    path('Blinds/',views.Blinds,name='Blinds'),
    path('wallTowall/',views.wallTowall,name='wallTowall'),
   
    
]