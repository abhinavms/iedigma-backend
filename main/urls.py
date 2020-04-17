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
from .views import anagram_lvl6, anagram_thetitanicdisaster
from .views import listen_to_the_sounds, listen_to_the_ekac
from .views import raseac_chaibefourcoffee, raseac_reputation
from .views import that_was_awesome, that_was_unexpected
from .views import welcometo_keyboard, welcometo_thepast
from .views import sdrawkcab_lvl11_kfc, sdrawkcab_lvl11_marathon, sdrawkcab_lvl11_nohtaram
from .views import take_a_breakn_dance, take_a_breakn_stop
from .views import lvl13_stop_singing, lvl13_stop_thatwasntthathard
from .views import lvl14_now_what, lvl14_now_mumbaiminute, lvl14_now_newyorkminute
from .views import lvl15_moredots_anddashes, lvl15_moredots_8547393808
from .views import success_but_onefinaldetail

urlpatterns = [
    path(r'', index_page, name='home'),
    path(r'about', about_page, name='about'),
    path(r'rules', rules_page, name='rules'),

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

    path(r'anagram/lvl6', anagram_lvl6, name='level6'),
    path(r'anagram/thetitanicdisaster', anagram_thetitanicdisaster, name='level6a'),
    
    path(r'listen/to/the/sounds', listen_to_the_sounds, name='level7'),
    path(r'listen/to/the/ekac', listen_to_the_ekac, name='level7a'),

    path(r'raseac/reputation', raseac_reputation, name='level8'),
    path(r'raseac/chaibefourcoffee', raseac_chaibefourcoffee, name='level8a'),

    path(r'that/was/awesome', that_was_awesome, name='level9'),
    path(r'that/was/unexpected', that_was_unexpected, name='level9a'),

    path(r'welcometo/thepast', welcometo_thepast, name='level10'),
    path(r'welcometo/keyboard', welcometo_keyboard, name='level10a'),

    path(r'sdrawkcab/lvl11/kfc', sdrawkcab_lvl11_kfc, name='level11'),
    path(r'sdrawkcab/lvl11/marathon', sdrawkcab_lvl11_marathon, name='level11a'),
    path(r'sdrawkcab/lvl11/nohtaram', sdrawkcab_lvl11_nohtaram, name='level11b'),

    path(r'take/a/breakn/dance', take_a_breakn_dance, name='level12'),
    path(r'take/a/breakn/stop', take_a_breakn_stop, name='level12a'),

    path(r'lvl13/stop/singing', lvl13_stop_singing, name='level13'),
    path(r'lvl13/stop/thatwasntthathard', lvl13_stop_thatwasntthathard, name='level13a'),

    path(r'lvl14/now/what', lvl14_now_what, name='level14'),
    path(r'lvl14/now/newyorkminute', lvl14_now_newyorkminute, name='level14a'),
    path(r'lvl14/now/mumbaiminute', lvl14_now_mumbaiminute, name='level14b'),

    path(r'lvl15/moredots/anddashes', lvl15_moredots_anddashes, name='level15'),
    path(r'lvl15/moredots/8547393808', lvl15_moredots_8547393808, name='level15a'),

    path(r'success/but/onefinaldetail', success_but_onefinaldetail, name='level15a'),

    path('admin/', admin.site.urls),
]

urlpatterns = urlpatterns + \
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'IEDIGMA'
admin.site.site_title = 'IEEE SCT SB : IEDIGMA'
