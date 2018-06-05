from PIL import Image
import zbarlight



"""
Realiza a leitura do QR CODE
"""
def get_qr(nome):
    """Realiza a leitura do qr code"""
    file_path = "votos/"
    caminho=file_path+nome
    with open(caminho, 'rb') as image_file:
        image = Image.open(image_file)
        image.load()

    codes = zbarlight.scan_codes(['qrcode'], image)
    final=codes[0].decode("utf-8")
    posicoes=final.replace("[","").replace("]","").replace(" ","").split(",")
    return posicoes
