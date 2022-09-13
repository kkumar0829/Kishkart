from django.urls import path

from cart.views import CartViews

urlpatterns = [
    path('cart/', CartViews.as_view()),
    path('cart/<int:id>', CartViews.as_view()),
    # path('getPrice/<int:product_id>', PriceViews.as_view())
]
