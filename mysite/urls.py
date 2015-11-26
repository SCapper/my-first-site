from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^register/', CreateView.as_view(
                        template_name='register.html',
                        form_class=UserCreationForm,
                        success_url='/')
    ),
    url(r'^accounts/', include('django.contrib.auth.urls')),
]
