from qrcode import QRCode
from qrcode.constants import ERROR_CORRECT_L, ERROR_CORRECT_H, ERROR_CORRECT_M, ERROR_CORRECT_Q


def make_code(text, error_correction_lvl=ERROR_CORRECT_M, back_color='#ffffff',
              fill_color='#000000', box_size=10, border=4, filename='code.png'):

    qr = QRCode(
        version=1,
        error_correction=error_correction_lvl,
        box_size=box_size,
        border=border,
    )
    qr.add_data(text)
    qr.make(fit=True)

    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    img.save(f'backend{filename}')
