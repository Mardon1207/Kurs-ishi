from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import stripe
from .models import Payment  # To‘lov modeli

@csrf_exempt  # CSRF tekshiruvini o‘chirib qo‘yish (faqat test uchun tavsiya qilinadi)
def create_checkout_session(request):
    # Faqat POST so‘rovlariga ruxsat beriladi
    if request.method != "POST":
        return JsonResponse({"xato": "Faqat POST so‘rovlariga ruxsat beriladi"}, status=405)

    # Foydalanuvchi tizimga kirganligini tekshiramiz
    if not request.user.is_authenticated:
        return JsonResponse({"xato": "Avtorizatsiya talab qilinadi"}, status=401)

    try:
        # Stripe orqali to‘lov sessiyasini yaratamiz
        session = stripe.checkout.Session.create(
            payment_method_types=["card"],  # Faqat karta orqali to‘lashga ruxsat
            line_items=[
                {
                    "price_data": {
                        "currency": "usd",  # To‘lov valyutasi
                        "product_data": {
                            "name": "Ijara to‘lovi",  # Mahsulot nomi
                        },
                        "unit_amount": 1000 * 100,  # 10 USD (Stripe sentlarda ishlaydi)
                    },
                    "quantity": 1,  # Mahsulot soni
                }
            ],
            mode="payment",  # To‘lov rejimi
            success_url="http://127.0.0.1:8000/payments/success/",  # To‘lov muvaffaqiyatli bo‘lsa, shu sahifaga yo‘naltiriladi
            cancel_url="http://127.0.0.1:8000/payments/cancel/",  # Foydalanuvchi to‘lovni bekor qilsa, shu sahifaga yo‘naltiriladi
        )

        # To‘lovni bazaga yozamiz
        payment = Payment.objects.create(
            user=request.user,  # Kim to‘lov qilayotganini saqlaymiz
            amount=10.00,  # To‘lov miqdori
            payment_status="pending"  # To‘lov holati (kutish rejimida)
        )

        # Stripe sessiya ID'sini qaytaramiz
        return JsonResponse({"sessiya_id": session.id})

    except Exception as e:
        return JsonResponse({"xato": str(e)}, status=400)  # Xatolik yuz bersa, uni qaytaramiz
