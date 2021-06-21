"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from django.views.generic import TemplateView
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import PostSitemap

sitemaps = {
    'post': PostSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name="base.html"), name="base"),
    # my pages
    path('blog/', include('blog.urls', namespace='blog')),
    # path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    # more pages
    path('404/', TemplateView.as_view(template_name="404.html"), name="404"),
    path('dashboard/', TemplateView.as_view(template_name="dashboard.html"), name="dashboard"),
    # to users
    path('account/', include('account.urls')),
    # to social
    path('social-auth/', include('social_django.urls', namespace='social')),
    # images
    path('images/', include('images.urls', namespace='images')),
    # to remove
    path('buttons/', TemplateView.as_view(template_name="to_remove/buttons.html"), name="buttons"),
    path('cards/', TemplateView.as_view(template_name="to_remove/cards.html"), name="cards"),
    path('tables/', TemplateView.as_view(template_name="to_remove/tables.html"), name="tables"),
    path('charts/', TemplateView.as_view(template_name="to_remove/charts.html"), name="charts"),
    path('animation/', TemplateView.as_view(template_name="to_remove/utilities-animation.html"), name="animation"),
    path('border/', TemplateView.as_view(template_name="to_remove/utilities-border.html"), name="border"),
    path('color/', TemplateView.as_view(template_name="to_remove/utilities-color.html"), name="color"),
    path('other/', TemplateView.as_view(template_name="to_remove/utilities-other.html"), name="other"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
