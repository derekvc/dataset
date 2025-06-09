import psutil
import pandas as pd
from datetime import datetime

# Lista para almacenar la información de cada proceso
procesos = []

# Iteramos sobre todos los procesos activos
for proc in psutil.process_iter(['pid', 'name', 'memory_info']):
    try:
        # Obtenemos la información de memoria (rss y vms) del proceso
        mem_info = proc.info['memory_info']
        procesos.append({
            'pid': proc.info['pid'],
            'nombre': proc.info['name'],
            'rss_MB': mem_info.rss / (1024 ** 2),  # Memoria física usada (RAM real)
            'vms_MB': mem_info.vms / (1024 ** 2)   # Memoria virtual asignada
        })
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        # Algunos procesos pueden cerrarse mientras se ejecuta el script o denegar acceso
        continue

# Crear el DataFrame con la información real de los procesos
df = pd.DataFrame(procesos)

# Guardar como archivo CSV con marca de tiempo
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
nombre_archivo = f'uso_ram_procesos_{timestamp}.csv'
df.to_csv(nombre_archivo, index=False)

print(f'Dataset generado correctamente: {nombre_archivo}')
print(df.head())