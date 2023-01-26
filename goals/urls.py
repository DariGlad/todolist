from django.urls import path

from goals import views


urlpatterns = [
    path('goal_category/create', views.GoalCategoryCreateView.as_view(), name='category_create'),
    path('goal_category/list', views.GoalCategoryCreateView.as_view(), name='category_list'),
    path('goal_category/<pk>', views.GoalCategoryCreateView.as_view(), name='category_detail'),
    path('goal/create', views.GoalCreateView.as_view(), name='goal_create'),
    path('goal/list', views.GoalCreateView.as_view(), name='goal_list'),
    path('goal/<pk>', views.GoalCreateView.as_view(), name='goal_detail'),
]
