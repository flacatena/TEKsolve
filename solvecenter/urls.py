from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('hardware',views.hardware_list, name='hardware_list'),
    path('software',views.software_list, name='software_list'),
    path('hardware_issues/<int:id>',views.hardware_issues,name='hardware_issues'),
    path('software_issues/<int:id>',views.software_issues,name='software_issues'),
    path('', TemplateView.as_view(template_name='base.html'),name='base_view'),
    path('show_hardware_resolution/<int:id>',views.show_hardware_resolution,name='show_hardware_resolution'),

]