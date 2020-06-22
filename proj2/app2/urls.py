from django.urls import path,re_path
from app2 import views
# template tagging
app_name = 'app2'

urlpatterns=[
    re_path(r'^users/',views.user,name='users'),
    re_path(r'^formpage/', views.FF, name='form_name'),
    re_path(r'^signup/', views.SU, name='form_model'),
    re_path(r'^register/$',views.register,name='register'),
    re_path(r'^logout/$',views.user_logout,name='logout'),
    re_path(r'^user_login/$',views.user_login,name='user_login')

]