from django.urls import path

from goals import views


urlpatterns = [
    path('goal_category/create', views.GoalCategoryCreateView.as_view(), name='category_create'),
    path('goal_category/list', views.GoalCategoryCreateView.as_view(), name='category_list'),
    path('goal_category/<pk>', views.GoalCategoryCreateView.as_view(), name='category_detail'),
]
