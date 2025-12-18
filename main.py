# Punto de entrada del programa
import os
import zipfile
import backup_manager

def comprimir_carpeta(carpeta, zip_final):
    zip_1 = zipfile.ZipFile(zip_final, 'w')
    for archivo in os.listdir(carpeta):
        zip_1.write(carpeta + "/" + archivo)
    zip_1.close()
#Si le das a iniciar se guarda ya la copia .zip FJ 19


carpeta_origen = "dades_importants"  # La carpeta que se quiere proteger
arxiu_seguretat = "copia_seguretat.zip"
carpeta_restauracio = "dades_recuperades"
print("Iniciant procés de Data Bunker ")

backup_manager.comprimir_carpeta(carpeta_origen, arxiu_seguretat)
backup_manager.restaurar_copia(arxiu_seguretat, carpeta_restauracio)
backup_manager.verificar_restauracio(carpeta_restauracio)

print("Procés finalitzat ")