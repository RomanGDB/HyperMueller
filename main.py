import serial

# Configura el puerto serial
ser = serial.Serial(
    port='COM3',          # Cambia esto por el puerto correcto
    baudrate=115200,      # Velocidad de baudios actualizada
    bytesize=serial.EIGHTBITS,  # 8 bits de datos
    parity=serial.PARITY_NONE,  # Sin paridad
    stopbits=serial.STOPBITS_ONE,  # 1 bit de parada
    timeout=1,            # Tiempo de espera para la respuesta
    xonxoff=False,        # Sin control de flujo de software
    rtscts=False,         # Sin control de flujo de hardware
    dsrdtr=False          # Sin DSR/DTR
)

# Enviar el comando 'INFO Z' seguido de un retorno de carro (\r)
#command = "1H WHERE Z \r"
#command = "1H MOVE Z=10000 \r"  # \r es el código para Carriage Return (0x0D)
#command = "2HB X = 1000 \r"
#command = "2H WHERE X Y \r"  # \r es el código para Carriage Return (0x0D)
#command = "1H MOVE Z=1000 \r"  # \r es el código para Carriage Return (0x0D)
#command = "3FMP \r"
#command = "2H WHERE X Y \r"  # \r es el código para Carriage Return (0x0D)
#command = "1H WHERE Z \r"  # \r es el código para Carriage Return (0x0D)

command = "2H MOVE X = 0 Y = 0 \r"  # \r es el código para Carriage Return (0x0D)
#command = "3FMP 6 \r"

command = "3FMP 2 \r"


ser.write(command.encode())  # Envía el comando codificado en ASCII

print("Comando enviado:", command.encode())

# Leer la respuesta del dispositivo
response = ser.readline()  # Lee hasta encontrar un retorno de carro/nueva línea

# Convertir y mostrar la respuesta en decimal
print("Respuesta en bytes:", response)

# Cerrar el puerto serial
ser.close()
