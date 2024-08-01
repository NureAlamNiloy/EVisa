from django.shortcuts import render, redirect
from rest_framework import views, response, status
import stripe
from django.conf import settings

# Create your views here.

stripe.api_key = settings.STRIPE_SECRET_KEY

class StripeCheckoutView(views.APIView):
    def post(self, request, *args, **kwargs):
        try:
            checkout_session = stripe.checkout.Session.create(
                line_items=[
                    {
                        # 'price': 'prod_QZhNxBAWdw7g14',
                        'price': 'price_1PiXyYRslcMqi7b5zfd0E67w',
                        'quantity': 1,
                    },
                ],
                # payment_method_types = ['card'],
                mode='payment',
                success_url='http://localhost:5173' + '/success=true&session_id={CHECKOUT_SESSION_ID}',
                cancel_url= 'http://localhost:5173'+ '/canceled=true',
            )
            return redirect(checkout_session.url)
        except Exception as e:
            return str(e)




class StripeWebhookView(views.APIView):
    def post(self, request, *args, **kwargs):
        payload = request.body
        sig_header = request.META.get('HTTP_STRIPE_SIGNATURE')
        event = None

        try:
            event = stripe.Webhook.construct_event(
                payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
            )
        except ValueError as e:
            # Invalid payload
            return response.Response(status=status.HTTP_400_BAD_REQUEST)
        except stripe.error.SignatureVerificationError as e:
            # Invalid signature
            return response.Response(status=status.HTTP_400_BAD_REQUEST)

        # Handle the event
        if event['type'] == 'checkout.session.completed':
            session = event['data']['object']
            user_payment = UserPayment.objects.get(checkOut_id=session['id'])
            user_payment.is_payment = True
            user_payment.save()

        return response.Response(status=status.HTTP_200_OK)