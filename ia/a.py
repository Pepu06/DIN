import subprocess

# Nombre del archivo donde se guardará la lista de librerías
requirements_path = 'requirements.txt'

# Ejecuta el comando para listar las librerías instaladas y escribe el resultado en el archivo
with open(requirements_path, 'w') as file:
    subprocess.run(['pip', 'freeze'], stdout=file)

print(f"El archivo {requirements_path} se ha generado correctamente.")
