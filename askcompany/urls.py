from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.conf import settings

# def mysum(request, x, y):
#     result = x + y
#     return HttpResponse('result = {}'.format(result))

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/', include('shop.urls')),
    path('blog/', include('blog.urls')),
    # path('mysum/<int:x>/<int:y>/', mysum),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns