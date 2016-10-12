from django.conf.urls import url
from django.contrib import admin

import test
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^aaa/',test.httpres),
]
