#------ Torres - DDN MOox - API rotacion --- Preparacion de BD ------- 21/12/22 -----
#------------------------------------------------------------------------------------
#------------------------- Rotacion, almacenamiento auto ----------------------------
#------------------------------------------------------------------------------------
#-Carpetas necesarias: Roted>Roted    -------- Imagen nueva cada: 10° ---------------
#-------------------------- >RotedAdd -----------------------------------------------

import cv2
import numpy as np


cont=0
muestra='>>.'

for i in range (12,69):

    if i==20 or i==30 or i==40 or i==50 or i==60:
        i=i+1
         
    name = str(i)

    image = cv2.imread("./Micrografias/S" + name + '.png')
    ancho = image.shape[1] #columnas 
    alto = image.shape[0] # filas
    muestra=muestra + '.'
    print(muestra)

    for j in range (1,36):
        
        rot=j*10
        aux=str(rot)
        # Rotación 5
        M = cv2.getRotationMatrix2D((ancho//2,alto//2),rot,1)
        imageOut = cv2.warpAffine(image,M,(ancho,alto))

        imageOutaux = cv2.add(imageOut, image)

        #cv2.imshow('Imagen de entrada',image)
        #cv2.imshow('Imagen de salida',imageOutaux)

        cv2.imwrite("./Roted/Roted/" +'S' + name + '_Rot_' + aux + '.png', imageOut)
        cv2.imwrite("./Roted/RotedAdd/" +'S' + name + '_RotAdd_' + aux + '.png', imageOutaux)
        cont=cont+1
        #cv2.waitKey(0)


print(">>> Proceso terminado: " + str(cont) + " imagenes añadidas a las carpetas :)")

cv2.destroyAllWindows()