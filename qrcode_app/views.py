from django.shortcuts import render
from .models import QRCode
import qrcode
from django.shortcuts import render, redirect, get_object_or_404
from django.core.files.base import ContentFile
import io

def generate_qr(request):
    qr_code_url = None
    qr_code_download_url = None

    if request.method == 'POST':
        text = request.POST.get('text')
        if text:
            qr = qrcode.QRCode(
                version=None,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(text)
            qr.make(fit=True)
            img = qr.make_image(fill='black', back_color='white')

            buffer = io.BytesIO()
            img.save(buffer, format="PNG")
            qr_code_image = ContentFile(buffer.getvalue(), 'qrcode.png')

            qr_code = QRCode.objects.create(text=text)
            qr_code.qr_image.save('qrcode.png', qr_code_image)

            qr_code_url = qr_code.qr_image.url
            qr_code_download_url = qr_code.qr_image.url

    return render(request, 'qrcode_app/index.html', {
        'qr_code_url': qr_code_url,
        'qr_code_download_url': qr_code_download_url
    })

def manage_qr_codes(request):
    qr_codes = QRCode.objects.all()

    if request.method == 'POST':
        qr_code_id = request.POST.get('qr_code_id')
        qr_code = get_object_or_404(QRCode, id=qr_code_id)
        qr_code.qr_image.delete()
        qr_code.delete()

        return redirect('manage_qr_codes')
    
    return render(request, 'qrcode_app/manage_qr_codes.html', {'qr_codes': qr_codes})