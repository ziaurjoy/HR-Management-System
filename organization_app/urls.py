from django.urls import path, include
from .views import mother_organization_views, sister_organization_views, branch_views

mother_organization_patterns=[
    path('create/', mother_organization_views.mother_organization_create_view, name='mother-organization-create'),
    path('index/', mother_organization_views.mother_organization_index_view, name='mother-organization-index'),
    path('update/<int:pk>', mother_organization_views.mother_organization_update_view, name='mother-organization-update'),
    path('delete/<int:pk>', mother_organization_views.mother_organization_delete_view, name='mother-organization-delete'),
]

sister_organization_patterns=[
    path('create/', sister_organization_views.sister_organization_create_view, name='sister-organization-create'),
    path('index/', sister_organization_views.sister_organization_index_view, name='sister-organization-index'),
    path('update/<int:pk>', sister_organization_views.sister_organization_update_view, name='sister-organization-update'),
    path('delete/<int:pk>', sister_organization_views.sister_organization_delete_view, name='sister-organization-delete'),

    path('load-organization', sister_organization_views.ajax_load_sister_organization, name='ajax-load-sister-organization'),
]

branch_patterns=[
    path('create/', branch_views.branch_create_view, name='branch-create'),
    path('index/', branch_views.branch_index_view, name='branch-index'),
    path('update/<int:pk>', branch_views.branch_update_view, name='branch-update'),
    path('delete/<int:pk>', branch_views.branch_delete_view, name='branch-delete'),
    path('load-branches', branch_views.ajax_load_branch, name='ajax-load-branches'),
]


urlpatterns = [
    path('mother/', include(mother_organization_patterns)),
    path('sister/', include(sister_organization_patterns)),
    path('branch/', include(branch_patterns)),
]