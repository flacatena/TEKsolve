from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='base.html'),name='base_view'),
    path('hardware_list',views.hardware_list, name='hardware_list'),
    path('software_list',views.software_list, name='software_list'),
    path('show_hardware_issues/<int:id>',views.hardware_issues,name='show_hardware_issues'),
    path('show_software_issues/<int:id>',views.software_issues,name='show_software_issues'),
    path('show_hardware_resolution/<int:id>',views.show_hardware_resolution,name='show_hardware_resolution'),
    path('show_software_resolution/<int:id>',views.show_software_resolution, name='show_software_resolution'),
    path('display_issues_without_res',views.display_issues_without_res,name='display_issues_without_res'),
    path('enter_new_resolution/<int:id>',views.enter_new_resolution,name='enter_new_resolution'),
    path('enter_new_issue', views.enter_new_issue, name='enter_new_issue'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)