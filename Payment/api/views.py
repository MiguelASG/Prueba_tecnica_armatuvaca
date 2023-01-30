from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from .models import Payment
import json
import stripe
from django.conf import settings
stripe.api_key = settings.SECRET_KEY

# Create your views here.



class PaymentView(View):

	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		return super().dispatch(request, *args, **kwargs)


	"""def get(self, request, id=0):
		if(id>0): 
			payments=list(Payment.objects.filter(id=id).values())
			if len(payments)>0:
				resultado = {'message':"Petición Completada", 'payments':payments[0]}
			else: 
				resultado = {'message':"Not Found"}
			return JsonResponse(resultado)
		else:
			payments = list(Payment.objects.values())
			if len(payments)>0:
				resultado = {'message':"Petición Completada", 'payments':payments}
			else: 
				resultado = {'message':"Not Found"}
			return JsonResponse(resultado)
	"""

	def post(self, request):
		jd=json.loads(request.body)
		temp = jd['card_number'].replace(" ","")
		resultado = {'message':''}
		if(len(temp)<16):
			resultado['message'] = 'Transaccion rechazada, el número de tarjeta tiene menos de 16 digitos'
		elif(jd['total_value']<1000):
			resultado['message'] = 'Transaccion rechazada, el Valor total debe ser mayor o igual a $1000'
		elif(len(str(jd['card_cvv']))!=3):
			resultado['message'] = 'Transaccion rechazada, el codigo de seguridad debe tener 3 digitos'
		else:
			int(temp)
			cn = ('*'*(len(temp)-4))+temp[-4:]
			cm = jd["total_value"]*0.03
			cm = jd["total_value"]+cm+cm*0.19
			cm = cm-cm*0.015
			stripe.PaymentIntent.create(
	        	currency = "USD",
	            amount = int(cm),
	            receipt_email = jd["name"] + jd["surname"] + "@mail.com",
	            description = jd["extra_description"]
        		)
			Payment.objects.create(
				name=jd['name'],
				surname=jd['surname'],
				card_number=cn,
				card_cvv=jd['card_cvv'],
				total_value=jd['total_value'],
				extra_description=jd['extra_description'],
				comission_value = cm
				)
			resultado['message']="Petición Completada"
		return JsonResponse(resultado)

	"""def payToStripe(jd):
		stripe.PaymentIntent.create(
        	currency = "USD",
            amount = jd["total_value"],
            email = jd["name"] + jd["surname"] + "@mail.com",
            description = jd["extra_description"]
        )



	def calcularCm(valor):
		cm = valor*0.03
		cm = valor+cm+cm*0.19
		cm = cm-cm*0.015
		return cm
"""
	def put(self, request):
		pass

	def delete(self, request):
		pass



	