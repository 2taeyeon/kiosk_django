from django.urls import path
from .views import DrinkListView, DrinkDetailView


app_name = "kiosk"
urlpatterns = [
    # path("", views.index, name="index"),
    path("", DrinkListView.as_view(), name="drink_list"),  # 음료 카테고리 페이지
    path("<int:pk>/", DrinkDetailView.as_view(), name="drink_detail"),
]
