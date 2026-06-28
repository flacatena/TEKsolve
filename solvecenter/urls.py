from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='base.html'),name='base_view'),
    path('hardware_list',views.hardware_list, name='hardware_list'),
    path('software_list',views.software_list, name='software_list'),
    path('show_hardware_issues/<int:id>',views.hardware_issues,name='show_hardware_issues'),
    path('show_software_issues/<int:id>',views.software_issues,name='show_software_issues'),
    path('show_hardware_resolution/<int:id>',views.show_hardware_resolution,name='show_hardware_resolution'),
    path('show_software_resolution/<int:id>',views.show_software_resolution, name='show_software_resolution'),
]