#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       pileffects.py
#       
#       Copyright 2014 Recursos Python - www.recursospython.com
#       
from PIL import Image, ImageChops, ImageEnhance, ImageOps
def main():
    image = Image.open("image.jpg")
    
    # Invertir colores.
    new_image = ImageChops.invert(image)
    new_image.save("image_1.jpg")
    
    # Escala de grises.
    new_image = ImageOps.grayscale(image)
    new_image.save("image_2.jpg")
    
    # Resaltar luces.
    new_image = ImageEnhance.Brightness(image).enhance(2)
    new_image.save("image_3.jpg")
    
    # Contraste.
    new_image = ImageEnhance.Contrast(image).enhance(4)
    new_image.save("image_4.jpg")
    
    # Espejo.
    new_image = ImageOps.mirror(image)
    new_image.save("image_5.jpg")
    
    # Cambiar tamaño.
    new_image = image.resize((320, 240))
    new_image.save("image_6.jpg")
    
    # Diminuir nitidez.
    new_image = ImageEnhance.Sharpness(image).enhance(-4)
    new_image.save("image_7.jpg")
    
if __name__ == "__main__":
    main()
