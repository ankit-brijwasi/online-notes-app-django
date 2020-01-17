from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from notes import views as notes_views
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', auth_views.LoginView.as_view(
        template_name="users/login.html",
        redirect_authenticated_user=True
    ), name="user-login"),
    path('logout/', auth_views.LogoutView.as_view(template_name="users/logout.html"), name="user-logout"),
    path('register/', views.register, name="user-register"),

    # path('user/profile/', views.edit_profile, name="user-profile"),    
    path('create/', notes_views.NotesCreateView.as_view(), name="create-notes"),
    path('view', notes_views.NotesListView.as_view(), name="view-all"),
    path('<int:pk>/view/', notes_views.NotesDetailView.as_view(), name="view-specific"),
    path('<int:pk>/update/', notes_views.NotesUpdateView.as_view(), name="update-notes"),
    path('<int:pk>/delete/', notes_views.NotesDeleteView.as_view(), name="delete-notes"),
    path('settings/', views.settings, name="settings"),
    path('settings/change-password/', views.changePassword, name="change-password"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)