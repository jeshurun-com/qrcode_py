from django.db import models
from django.db import models

class QRCode(models.Model):
    text = models.CharField(max_length=255)
    qr_image = models.ImageField(upload_to='qrcodes/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"QR Code for: {self.text[:50]}"