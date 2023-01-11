from django.urls import path
from . import views

urlpatterns = [
    path('', views.DocsList.as_view(), name='docs_home'),
    path('create', views.DocsCreateView.as_view(), name='create'),
    path('<int:pk>', views.DocsDetailView.as_view(), name='docs-detail'),
    path('<int:pk>/edit', views.DocsUpdateView.as_view(), name='docs-edit'),
    path('<int:pk>/delete', views.DocsDeleteView.as_view(), name='docs-delete'),
    path('informed', views.UserInformedList.as_view(), name='informed')

]