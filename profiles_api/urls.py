from django.urls import path, include

from rest_framework.routers import DefaultRouter

from profiles_api import views

# To register ViewSet, need to do it thru Router
router = DefaultRouter()
router.register("hello-viewset", views.HelloViewSet, base_name="hello-viewset")

urlpatterns = [
    path("hello-view/", views.HelloApiView.as_view()),  # This is to register API Views
    path(
        "", include(router.urls)
    ),  # This is to register ViewSet -- Note: "" refers to empty prefix on the urls
]
