from django.urls import path
from . import views
app_name = 'pages'
urlpatterns = [
    path('', views.index, name='index'),
path('v', views.vipechka, name='vipechka'),
path('s', views.salat, name='salat'),
path('d', views.desert, name='desert'),
path('n', views.napitki, name='napitki'),
path('g', views.galler, name='gallery'),
path('so', views.sobitiya, name='sobitiya'),
path('k', views.komanda, name='komanda'),
path('vak', views.vakansii, name='vakansii'),
path('o', views.otzivi, name='otzivi'),
path('gde', views.gde, name='gde'),
path('dv', views.d_vipech, name='d_vipech'),
path('dc', views.d_coffee, name='d_coffee'),
path('drc', views.d_r_cafe, name='d_r_cafe'),
path('de', views.d_eclair, name='d_eclair'),
path('mk', views.m_k, name='m_k'),
path('cart', views.cart, name='cart'),
path('p', views.cart, name='product_detail'),
]