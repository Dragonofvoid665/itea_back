from django.urls import path
from project_iteea import views
urlpatterns = [
    path('categories/',views.Category_of_coursesView.as_view()),
    path('mentors/', views.MentorsView.as_view()),
    path('vacansy/',views.VacansyView.as_view()),
    path('news/',views.NewsView.as_view()),
    path('categories/<int:category_id>/',views.Category_of_courseView),
    path('news/register/',views.EmailView),
    path('email/',views.EmailViews.as_view())
]
