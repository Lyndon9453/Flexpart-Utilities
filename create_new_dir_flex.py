#!/usr/bin/python3
# Author: Ing. Mauro Gonzalez
# Date: 09/2019

import shutil
import os
import sys
destiny = '/home/mgonzalez/CORRIDAS_FLEXPART/'  # RUTA DE DESTINO
# format_destiny: /home/%USER%/
source = '/home/mgonzalez/Descargas/fptraining2019/flexpart_v10.3.1_3cd0f17/'  # RUTA DE LA FUENTE DE DATOS
# format_source: /home/%USER%/%FLEXPART_DIRECTORY/

if os.path.isdir(destiny):
    nombre = input('Ingresar nombre identificatorio de carpeta: ')
    while os.path.isdir(destiny+nombre):
        print('Directorio ya existe!')
        nombre = input('Elegir otro nombre: ')
    destiny += nombre
    if os.path.isdir(source):
        shutil.copytree('%soptions' % source, destiny + '/options')
        shutil.copytree('%soutput' % source, destiny + '/output')
        print('Carpeta creada con exito. Archivos copiados correctamente.\nPath: %s'%destiny)
    else:
        print('ERROR AL CREAR CARPETA\nChequear ruta de FUENTE DE DATOS\n'
              'help: gedit \'Creador Ficheros Flexpart.py\' y editar \'source\' ')
        sys.exit()
else:
    print('ERROR AL CREAR CARPETA\nChequear ruta de DESTINO\n'
          'help: gedit \'Creador Ficheros Flexpart.py\' y editar \'destiny\' ')
    sys.exit()

