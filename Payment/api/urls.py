from django.urls import path
from .views import PaymentView	

urlpatterns= [
	path('payment/', PaymentView.as_view(), name='payment_list'),
	path('payment/<int:id>', PaymentView.as_view(), name='payment_sub')

]