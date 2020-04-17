"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import index_page, about_page, rules_page

from .views import playwithme_level1, playwithme_level2
from .views import empty_level2, full_level2
from .views import googleit_lvl3, googleit_mandymoore, googleit_onlyhope
from .views import z2o_onlyhope_level4, z2o_congo_level4
from .views import draw_the_line_level5, draw_the_line_800x600

urlpatterns = [
    path(r'', index_page, name='home'),
    path(r'about', about_page, name='about'),
    path(r'rules', rules_page, name='rule'),

    path(r'playwithme/level1', playwithme_level1, name='level1'),
    path(r'playwithme/level2', playwithme_level2, name='level1a'),

    path(r'empty/level2', empty_level2, name='level2'),
    path(r'full/level2', full_level2, name='level2a'),
    
    path(r'googleit/lvl3', googleit_lvl3, name='level3'),
    path(r'googleit/mandymoore', googleit_mandymoore, name='level3a'),
    path(r'googleit/onlyhope', googleit_onlyhope, name='level3b'),
    
    path(r'z2o/onlyhope/level4', z2o_onlyhope_level4, name='level4'),
    path(r'z2o/congo/level4', z2o_congo_level4, name='level4a'),
    
    path(r'draw/the/line/level5', draw_the_line_level5, name='level5'),
    path(r'draw/the/line/800x600', draw_the_line_800x600, name='level5a'),


    path('admin/', admin.site.urls),
]

urlpatterns = urlpatterns + \
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'IEDIGMA'
admin.site.site_title = 'IEEE SCT SB : IEDIGMA'
