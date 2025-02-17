# from django.contrib import admin
# from django.urls import path,include
# from api.views import CompanyViewSet, EmployeeViewSet
# from rest_framework import routers


# router = routers.DefaultRouter()
# router.register(r'companies', CompanyViewSet)
# router.register(r'employees', EmployeeViewSet)


# urlpatterns = [
#     path('',include(router.urls))


# ]
# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import CompanyViewSet, EmployeeListCreateView, EmployeeUpdateDestroyView

# # Create a router and register our viewset with it.
# router = DefaultRouter()
# router.register(r'companies', CompanyViewSet, basename='company')

# urlpatterns = [
#     path('', include(router.urls)),  # Include the router URLs for CompanyViewSet
#     path('employees/', EmployeeListCreateView.as_view(), name='employee_list'),  
#     path('employees/<int:pk>/', EmployeeUpdateDestroyView.as_view(), name='employee_detail'), 
# ]


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CompanyViewSet, EmployeeListCreateView, EmployeeUpdateDestroyView

# Create a router and register our viewset with it.
router = DefaultRouter()
router.register(r'companies', CompanyViewSet, basename='company')


urlpatterns = [
    path('', include(router.urls)),  # Include the router URLs for CompanyViewSet
    path('employees/', EmployeeListCreateView.as_view(), name='employee_list'),  
    path('employees/<int:pk>/', EmployeeUpdateDestroyView.as_view(), name='employee_detail'), 
]