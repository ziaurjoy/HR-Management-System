from django.urls import path, include
from .views import registration_views, permission_views



branch_admin_registration_patterns=[
    path('create/', registration_views.registration_branch_admin_create_view, name='branch-admin-registration-create'),
    # path('index/', registration_views.branch_index_view, name='branch-index'),
    # path('update/<int:pk>', registration_views.branch_update_view, name='branch-update'),
    # path('delete/<int:pk>', registration_views.branch_delete_view, name='branch-delete'),
    path('ajax-load-branch-user/', registration_views.load_branch_user, name='ajax-load-branch-users'),
    
]

sister_admin_registration_patterns=[
    path('create/', registration_views.registration_sister_admin_create_view, name='sister-admin-registration-create'),
    # path('index/', registration_views.branch_index_view, name='branch-index'),
    # path('update/<int:pk>', registration_views.branch_update_view, name='branch-update'),
    # path('delete/<int:pk>', registration_views.branch_delete_view, name='branch-delete'),
]

mother_admin_registration_patterns=[
    path('create/', registration_views.registration_mother_admin_create_view, name='mother-admin-registration-create'),
    # path('index/', registration_views.branch_index_view, name='branch-index'),
    # path('update/<int:pk>', registration_views.branch_update_view, name='branch-update'),
    # path('delete/<int:pk>', registration_views.branch_delete_view, name='branch-delete'),
]

user_wise_permission_patterns=[
    path('permission', permission_views.user_wise_permissions_view, name='user-wise-permission'),
    path('permission/load', permission_views.load_user_wise_permission, name='ajax-load-user-wise-permission'),
    # path('permission/index', permission_views.user_permission_index_view, name='user-wise-permission-index'),
    # path('update/<int:pk>', registration_views.branch_update_view, name='branch-update'),
    # path('delete/<int:pk>', registration_views.branch_delete_view, name='branch-delete'),
]




urlpatterns = [
    path('registration/branch/', include(branch_admin_registration_patterns)),
    path('registration/sister/', include(sister_admin_registration_patterns)),
    path('registration/mother/', include(mother_admin_registration_patterns)),

    path('user-wise/', include(user_wise_permission_patterns)),
]