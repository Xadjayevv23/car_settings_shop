from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = i18n_patterns(
    path('account/', include('registration.backends.default.urls')),
    path('admin/', admin.site.urls),
    path('shop/', include('product.urls', namespace='products')),
    path('blog/', include('blog.urls', namespace='blogs')),
    path('', include('pages.urls', namespace='pages')),

)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
