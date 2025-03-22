from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(max_length=20, choices=[("pending", "Pending"), ("completed", "Completed"), ("failed", "Failed")], default="pending")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.amount} USD - {self.payment_status}"
