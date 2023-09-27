from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("test", views.test, name="test"),
    path('download-pdf', views.download_pdf_from_template, name="generate_pdf"),
    path('generate-pdf', views.generate_pdf_from_template, name="generate_pdf"),
]
