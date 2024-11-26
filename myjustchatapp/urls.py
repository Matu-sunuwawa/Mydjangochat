# First way of expression...

# from django.contrib import admin
# from django.urls import path

# from chat.views import index

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path("", index, name="index"),
# ]


# Second way of expression...
# from django.contrib import admin
# from django.urls import path, include

# from chat.views import index

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path("chat/", include("chat.urls", namespace='chat')),
# ]


from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("chat/", include("chat.urls")),
]