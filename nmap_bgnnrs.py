'''
coded by:
  _         _      _  _     _               _    
 | |__     (_)    | || |   (_)    __ __    (_)   
 | '_ \    | |     \_, |   | |    \ V /    | |   
 |_.__/   _|_|_   _|__/   _|_|_   _\_/_   _|_|_  
_|"""""|_|"""""|_| """"|_|"""""|_|"""""|_|"""""| 
"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-' 
'''




import os 
import time
import colorama
from colorama import Fore
from colorama import Style
from tqdm import tqdm








def barra():
    loop= tqdm(total = 7000, position=0, leave=False)
    for k in range(7000):
        loop.set_description(Fore.MAGENTA+"Cargando...".format(k))
        loop.update(1)
    loop.close()



#limpiar terminal
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  
        command = 'cls'
    os.system(command)

clearConsole()


def distro():
    dist=int(input(Fore.RED+ Style.BRIGHT +'''

                                         )  (  (    (
                                         (  )  () @@  )  (( (
                                     (      (  )( @@  (  )) ) (
                                   (    (  ( ()( /---\   (()( (
     _______                            )  ) )(@ !O O! )@@  ( ) ) )
    <   ____)                      ) (  ( )( ()@ \ o / (@@@@@ ( ()( )
 /--|  |(  o|                     (  )  ) ((@@(@@ !o! @@@@(@@@@@)() (
|   >   \___|                      ) ( @)@@)@ /---\-/---\ )@@@@@()( )
|  /---------+                    (@@@@)@@@( // /-----\ \\ @@@)@@@@@(  .
| |    \ =========______/|@@@@@@@@@@@@@(@@@ // @ /---\ @ \\ @(@@@(@@@ .  .
|  \   \\=========------\|@@@@@@@@@@@@@@@@@ O @@@ /-\ @@@ O @@(@@)@@ @   .
|   \   \----+--\-)))           @@@@@@@@@@ !! @@@@ % @@@@ !! @@)@@@ .. .
|   |\______|_)))/             .    @@@@@@ !! @@ /---\ @@ !! @@(@@@ @ . .
 \__==========           *        .    @@ /MM  /\O   O/\  MM\ @@@@@@@. .
    |   |-\   \          (       .      @ !!!  !! \-/ !!  !!! @@@@@ .
    |   |  \   \          )   -biyivi- .  @@@@ !!     !!  .(. @.  .. .
    |   |   \   \        (    /   .(  . \)). ( |O  )( O! @@@@ . )      .
    |   |   /   /         ) (      )).  ((  .) !! ((( !! @@ (. ((. .   .
    |   |  /   /   ()  ))   ))   .( ( ( ) ). ( !!  )( !! ) ((   ))  ..
    |   |_<   /   ( ) ( (  ) )   (( )  )).) ((/ |  (  | \(  )) ((. ).
____<_____\\__\__(___)_))_((_(____))__(_(___.oooO_____Oooo.(_(_)_)((_

'''+ Style.RESET_ALL+Fore.YELLOW+'''
Elige una opcion: 
'''+Fore.RED+'''1)'''+Style.RESET_ALL+Fore.YELLOW+Style.BRIGHT+'''Linux
'''+Fore.RED+'''2)'''+Style.RESET_ALL+Fore.YELLOW+Style.BRIGHT+'''Termux 
'''+Style.RESET_ALL+          
Fore.GREEN+">>> "))
    if dist==1:
        barra()
        os.system("sudo apt install sl")
        clearConsole()
        os.system("sl")
        time.sleep(2)
    elif dist==2:
        barra()
        os.system("pkg install sl")
        clearConsole()
        os.system("sl")  
        time.sleep(2)

    else:
        print("")
        print("Error ingrese una opcion valida(ej. '1' , '2') ")  
        print("")
        time.sleep(2)
        distro()

distro()

#respuesta1
def resp():

    preg=int(input(Fore.LIGHTYELLOW_EX+'''
Ver información:
'''+
Fore.GREEN+'''1)'''+Style.RESET_ALL+Fore.BLUE+'''Si
'''+Style.RESET_ALL+
Fore.GREEN+'''2)'''+Style.RESET_ALL+Fore.BLUE+'''No(ejecutar comando)
'''+Style.RESET_ALL+
Fore.GREEN+'''3)'''+Style.RESET_ALL+Fore.BLUE+'''Regresar al menu principal
'''+Style.RESET_ALL+Fore.RED+
'''>>'''+Style.RESET_ALL))
    if preg==1:
        print('''
Escanear Hostname o IP:

La versatilidad de Nmap nos ofrece la opción de realizar el escaneo 
tanto mediante hostname como por IP, por lo que las dos líneas de 
comando tendrán el mismo resultado

comando utilizado: nmap <Ip> o <Hostname> 
ejemplo: nmap 127.0.0.1 o nmap "nombre del host"
''')
    
        resp()

    elif preg==2:
        Ip_Host=input("Ingresar Hostname o la Ip: ")
        os.system("nmap "+Ip_Host)
        time.sleep(2)
        resp()
    elif preg==3:
        banner()
    else:
        print("")
        print("Error ingrese una opcion valida(ej. '1' , '2' o '3') ")
        print("")
        time.sleep(2)
        resp()
        



#respuesta 2
def resp2():
  
    preg=int(input(Fore.LIGHTYELLOW_EX+'''
Ver información:
'''+
Fore.GREEN+'''1)'''+Style.RESET_ALL+Fore.BLUE+'''Si
'''+Style.RESET_ALL+
Fore.GREEN+'''2)'''+Style.RESET_ALL+Fore.BLUE+'''No(ejecutar comando)
'''+Style.RESET_ALL+
Fore.GREEN+'''3)'''+Style.RESET_ALL+Fore.BLUE+'''Regresar al menu principal
'''+Style.RESET_ALL+Fore.RED+
'''>>'''+Style.RESET_ALL))
    if preg==1:

        print('''
Escaneo de puertos TCP básico:

Esta opción analiza y muestra todos los puertos TCP (Transmission Control Protocol) 
reservados actualmente en la máquina destino.
-La opción -v significa “verbose”, por lo que se nos indica lo que está haciendo el análisis 
 al detalle

comando utilizado: nmap -v <Ip>
ejemplo: nmap -v 192.168.1.1''')
        time.sleep(2)
        resp2()

    elif preg==2:
        Ip=input("Ingresar Ip: ")
        os.system("nmap -v "+Ip)
        time.sleep(2)
        resp2()
    elif preg==3:
        banner()
    else:
        print("")
        print("Error ingrese una opcion valida(ej. '1' , '2' o '3') ")
        print("")
        time.sleep(2)
        resp2()
        



#respuesta 3
def resp3():
    
    preg=int(input(Fore.LIGHTYELLOW_EX+'''
Ver información:
'''+
Fore.GREEN+'''1)'''+Style.RESET_ALL+Fore.BLUE+'''Si
'''+Style.RESET_ALL+
Fore.GREEN+'''2)'''+Style.RESET_ALL+Fore.BLUE+'''No(ejecutar comando)
'''+Style.RESET_ALL+
Fore.GREEN+'''3)'''+Style.RESET_ALL+Fore.BLUE+'''Regresar al menu principal
'''+Style.RESET_ALL+Fore.RED+
'''>>'''+Style.RESET_ALL)) 

    if preg==1:
        print(''' 
Escanear un rango de IPs:

Escanear un rango de IPs nos resultaría útil en casos de un posible ataque de red.
si queremos intentar averiguar donde tiene lugar. También ahorraría tiempo al rastrear
este tipo de ataques. Se usa simplemente delimitando el último campo.
    
comando utilizado: nmap <IP>-<IP2>
ejemplo: nmap 192.168.1.1-103    
    
    ''')
        time.sleep(2)
        resp3()
    elif preg==2:
        Ip=input("Ingresar Ip: ")
        rango=input("Ingresar rango(ej. '-115'): ")
        os.system("nmap "+Ip+rango)
        time.sleep(2)
        resp3()
    elif preg==3:
        banner()
    else:
        print("")
        print("Error ingrese una opcion valida(ej. '1' , '2' o '3') ")
        print("")
        time.sleep(2)
        resp3()
        


#respuesta 4
def resp4():
   
    preg=int(input(Fore.LIGHTYELLOW_EX+'''
Ver información:
'''+
Fore.GREEN+'''1)'''+Style.RESET_ALL+Fore.BLUE+'''Si
'''+Style.RESET_ALL+
Fore.GREEN+'''2)'''+Style.RESET_ALL+Fore.BLUE+'''No(ejecutar comando)
'''+Style.RESET_ALL+
Fore.GREEN+'''3)'''+Style.RESET_ALL+Fore.BLUE+'''Regresar al menu principal
'''+Style.RESET_ALL+Fore.RED+
'''>>'''+Style.RESET_ALL)) 
    if preg==1:
        print('''
Escanear puertos concretos o rangos de puertos:

Este método de escaneo se centra en un puerto concreto. De esta forma, conseguiremos
que la salida sea más corta si no estamos interesados en otros.

comando utilizado: nmap-p <numero_puerto> <Ip>
ejemplo: nmap -p 80 192.168.1.200

De manera similar, delimitaremos el primer y último puerto para escanear rangos de puertos:

comando utilizado: nmap-p <numero_puerto_inicio>-<numero_puerto_final> <Ip>
ejemplo: nmap -p 80-995 192.168.1.200
    
    ''')
        time.sleep(2)
        resp4()
    elif preg==2:
        Ip=input("Ingresar Ip: ")
        pregrango=int(input('''1)Escanear solo un puerto
2)Escanear rango de puertos
'''+Fore.LIGHTRED_EX+">>>"+Style.RESET_ALL))
        if pregrango==1:

            puerto=input("Ingrese el numero del puerto: ")
            os.system("nmap -p "+puerto+" "+Ip)
        elif pregrango==2:
            puerto1=input("Ingrese el primer puerto: ")
            puerto2=input("Ingrese ultimo puerto: ")
            os.system("nmap -p "+puerto1+"-"+puerto2+" "+Ip)
        else:
            print("")
            print("Error ingrese una opcion valida(ej. '1' o '2') ")
            print("")
        time.sleep(2)
        resp4()
    elif preg==3:
        banner()    
    else:
        print("")
        print("Error ingrese una opcion valida(ej. '1' , '2' o '3') ")
        print("")
        time.sleep(2)
        resp4()
        


#respuesta 5 
def resp5():
    
    preg=int(input(Fore.LIGHTYELLOW_EX+'''
Ver información:
'''+
Fore.GREEN+'''1)'''+Style.RESET_ALL+Fore.BLUE+'''Si
'''+Style.RESET_ALL+
Fore.GREEN+'''2)'''+Style.RESET_ALL+Fore.BLUE+'''No(ejecutar comando)
'''+Style.RESET_ALL+
Fore.GREEN+'''3)'''+Style.RESET_ALL+Fore.BLUE+'''Regresar al menu principal
'''+Style.RESET_ALL+Fore.RED+
'''>>'''+Style.RESET_ALL)) 
    if preg==1:
        print(''' 

Escanear todos los puertos con Nmap:

Con este tipo de comando analizaremos los 65536 puertos disponibles en cada dispositivo. 
Este tipo de escaneo puede interesar a un administrador, pero desde luego no a un atacante. 
Primero, porque hace mucho ruido y segundo, porque normalmente ellos utilizan los conocidos 
como “half-opening” (canal a medio abrir).        
        
comando utilizado: nmap -p- localhost       

Con este comando veras todos los puertos actualmente detectados en tu equipo(abiertos o filtrados)   

        ''')
        time.sleep(2)
        resp5()
    elif preg==2:
        os.system("nmap -p- localhost")
        time.sleep(2)
        resp5()
    elif preg==3:
        banner()
    else:
        print("")
        print("Error ingrese una opcion valida(ej. '1' , '2' o '3') ")
        print("")
        time.sleep(2)
        resp5()    

#respuesta 6
def resp6():
   
    preg=int(input(Fore.LIGHTYELLOW_EX+'''
Ver información:
'''+
Fore.GREEN+'''1)'''+Style.RESET_ALL+Fore.BLUE+'''Si
'''+Style.RESET_ALL+
Fore.GREEN+'''2)'''+Style.RESET_ALL+Fore.BLUE+'''No(ejecutar comando)
'''+Style.RESET_ALL+
Fore.GREEN+'''3)'''+Style.RESET_ALL+Fore.BLUE+'''Regresar al menu principal
'''+Style.RESET_ALL+Fore.RED+
'''>>'''+Style.RESET_ALL))
    if preg==1:
        print('''

Lanzar un escaneo TCP SYN (opción por defecto):

Este comando determina si el puerto objetivo está escuchando. Mediante este comando se puede llevar a
cabo una técnica conocida como escaneo half-opening. Se le conoce así porque comienza como una conexión
normal, pero no llega a establecerse un handshake por ambas partes, sino que enviamos un único paquete
SYN y esperamos la respuesta.
Si el intérprete reciba una respuesta SYN/ACK  o RST (reset) sabrá marcar que el puerto está escuchando.        

comando utilizado: nmap-sS <IP>     
ejemplo: nmap -sS 192.168.1.200        

        ''')
        time.sleep(2)
        resp6()
    elif preg==2:
        Ip=input("Ingresar Ip: ")
        os.system("nmap -sS "+Ip)
        resp6()
    elif preg==3:
        banner()
    else:
        print("")
        print("Error ingrese una opcion valida(ej. '1' , '2' o '3') ")
        print("")
        time.sleep(2)
        resp6()

#respuesta 7
def resp7():
   
    preg=int(input(Fore.LIGHTYELLOW_EX+'''
Ver información:
'''+
Fore.GREEN+'''1)'''+Style.RESET_ALL+Fore.BLUE+'''Si
'''+Style.RESET_ALL+
Fore.GREEN+'''2)'''+Style.RESET_ALL+Fore.BLUE+'''No(ejecutar comando)
'''+Style.RESET_ALL+
Fore.GREEN+'''3)'''+Style.RESET_ALL+Fore.BLUE+'''Regresar al menu principal
'''+Style.RESET_ALL+Fore.RED+
'''>>'''+Style.RESET_ALL))  
    if preg==1:
        print('''

Escaneo de sistema operativo:
Es una opción simple que se limita a marcar el tipo de dispositivo, sistema operativo y MAC, entre otros datos.
Escogeremos la opción “O”

comando utilizado: nmap -O <IP>
ejemplo:nmap -O 192.168.43.45

''')
        time.sleep(2)
        resp7()
    if preg==2:
        Ip=input("Ingresar Ip: ")
        os.system("nmap -O "+Ip)
        time.sleep(2)
        resp7()
    elif preg==3:
        banner()
    else:
        print("")
        print("Error ingrese una opcion valida(ej. '1' , '2' o '3') ")
        print("")
        time.sleep(2)
        resp4()


#pregunta 8
def resp8():
   
    preg=int(input(Fore.LIGHTYELLOW_EX+'''
Ver información:
'''+
Fore.GREEN+'''1)'''+Style.RESET_ALL+Fore.BLUE+'''Si
'''+Style.RESET_ALL+
Fore.GREEN+'''2)'''+Style.RESET_ALL+Fore.BLUE+'''No(ejecutar comando)
'''+Style.RESET_ALL+
Fore.GREEN+'''3)'''+Style.RESET_ALL+Fore.BLUE+'''Regresar al menu principal
'''+Style.RESET_ALL+Fore.RED+
'''>>'''+Style.RESET_ALL))  
    if preg==1:
        print(''' 

Escaneo de Sistema Operativo y servicios:        

Escogeremos la opción “-A/a”.       
comando utilizado: nmap -A <IP>
ejemplo: nmap -A 192.168.1.43        
        
        
        
        ''')  
        time.sleep(2)
        resp8()  
    elif preg==2:
        Ip=input("Ingresar Ip: ")
        os.system("nmap -A "+Ip)
        time.sleep(2)
        resp8()
    elif preg==3:
        banner()
    else:
        print("")
        print("Error ingrese una opcion valida(ej. '1' , '2' o '3') ")
        print("")
        time.sleep(2)
        resp8()


#pregunta 9
def resp9():
   
    preg=int(input(Fore.LIGHTYELLOW_EX+'''
Ver información:
'''+
Fore.GREEN+'''1)'''+Style.RESET_ALL+Fore.BLUE+'''Si
'''+Style.RESET_ALL+
Fore.GREEN+'''2)'''+Style.RESET_ALL+Fore.BLUE+'''No(ejecutar comando)
'''+Style.RESET_ALL+
Fore.GREEN+'''3)'''+Style.RESET_ALL+Fore.BLUE+'''Regresar al menu principal
'''+Style.RESET_ALL+Fore.RED+
'''>>'''+Style.RESET_ALL))
    if preg==1:
        print('''

Escaneo de servicios estandar:

Si queremos evaluar únicamente los servicios con puerto asociado, es muy posible que la base de datos de Nmap 
(con más de 2000 entradas) encuentre algo interesante.
Puertos comunes como SSH (22), DNS (53) o HTTP (80) aparecerán listados.

comando ejecutado: nmap -sV <IP>
ejemplo: nmap -sV 192.168.1.43        

        ''')
        time.sleep(2)
        resp9()
    elif preg==2:
        Ip=input("Ingresar Ip: ")
        os.system("nmap -sV "+Ip)
        time.sleep(2)
        resp9()
    elif preg==3:
        banner()
    else:
        print("")
        print("Error ingrese una opcion valida(ej. '1' , '2' o '3') ")
        print("")
        time.sleep(2)
        resp9()

#pregunta 10 
def resp10():
   
    preg=int(input(Fore.LIGHTYELLOW_EX+'''
Ver información:
'''+
Fore.GREEN+'''1)'''+Style.RESET_ALL+Fore.BLUE+'''Si
'''+Style.RESET_ALL+
Fore.GREEN+'''2)'''+Style.RESET_ALL+Fore.BLUE+'''No(ejecutar comando)
'''+Style.RESET_ALL+
Fore.GREEN+'''3)'''+Style.RESET_ALL+Fore.BLUE+'''Regresar al menu principal
'''+Style.RESET_ALL+Fore.RED+
'''>>'''+Style.RESET_ALL))
    if preg==1:
        print('''

Escaneo de servicios agresivo:

Con un análisis de servicios más agresivo podemos obtener más información. Sin embargo, este escaneo 
deja más trazas en el sistema y en logs de firewalls, por lo que los hackers “black hat” normalmente 
no utilizan este tipo de escaneo.
Este método es útil para detectar servicios que no se están ejecutando en sus puertos predefinidos.

comando utilizado: nmap -sV --version-intensity 5 <IP>
ejemplo: nmap -sV --version-intensity 5 192.168.43.1                   
        ''')
        resp10()
    elif preg==2:
        Ip=input("Ingresar Ip: ")
        os.system("nmap -sV --version-intensity 5 "+Ip)
        time.sleep(2)
        resp10()
    elif preg==3:
        banner()
    else:
        print("")
        print("Error ingrese una opcion valida(ej. '1' , '2' o '3') ")
        print("")
        time.sleep(2)
        resp10()



#pregunta 11
def resp11():
    
    preg=int(input(Fore.LIGHTYELLOW_EX+'''
Ver información:
'''+
Fore.GREEN+'''1)'''+Style.RESET_ALL+Fore.BLUE+'''Si
'''+Style.RESET_ALL+
Fore.GREEN+'''2)'''+Style.RESET_ALL+Fore.BLUE+'''No(ejecutar comando)
'''+Style.RESET_ALL+
Fore.GREEN+'''3)'''+Style.RESET_ALL+Fore.BLUE+'''Regresar al menu principal
'''+Style.RESET_ALL+Fore.RED+
'''>>'''+Style.RESET_ALL))  
    if preg==1:
        print('''

Escaneo de servicios de banner ligero:

Un escaneo ligero de este tipo es usado normalmente por hackers cuando intentan permanecer en la sombra. 
Es mucho menos ruidoso que un escaneo agresivo y permite obtener datos sin llamar demasiado la atención, 
lo que aporta una clara ventaja.        
Este método no intenta detectar el servicio, sino que se limita a capturar el banner del servicio abierto 
para averiguar que se está ejecutando.        

comando utilizado:  nmap -sV --version-intensity 0 <IP>
ejemplo: nmap -sV --version-intensity 0 192.168.43.1         
        ''')
        resp11()
    elif preg==2:
        Ip=input("Ingresar Ip: ")
        os.system("nmap -sV --version-intensity 0 "+Ip)
        time.sleep(2)
        resp11()
    elif preg==3:
        banner()
    else:
        print("")
        print("Error ingrese una opcion valida(ej. '1' , '2' o '3') ")
        print("")
        time.sleep(2)
        resp11()


#pregunta 12
def resp12():
   
    preg=int(input(Fore.LIGHTYELLOW_EX+'''
Ver información:
'''+
Fore.GREEN+'''1)'''+Style.RESET_ALL+Fore.BLUE+'''Si
'''+Style.RESET_ALL+
Fore.GREEN+'''2)'''+Style.RESET_ALL+Fore.BLUE+'''No(ejecutar comando)
'''+Style.RESET_ALL+
Fore.GREEN+'''3)'''+Style.RESET_ALL+Fore.BLUE+'''Regresar al menu principal
'''+Style.RESET_ALL+Fore.RED+
'''>>'''+Style.RESET_ALL))  
    if preg==1:
        print('''

Escaneo de una subred completa:

Nmap es una herramienta extremadamente versátil y seguro que hay quien no la ha usado habitualmente para escanear 
redes en su conjunto. Pues bien, aquí nos ofrece resultados igual de buenos.
Básicamente, para realizar un escaneo de red completa con nmap tendremos ante todo que indicar el valor de la red
como argumento a través del número de bytes de su máscara de red. Es decir, si cuando analizamos un único host 
escribimos su dirección IP ej.: nmap <IP>. Ahora lo que haremos será indicar además la máscara de red.

comando utilizado: nmap <IP>/<Mascara_de_Red>
En esta pagina encontraras la forma en la que puedes calcular una mascara de subred para TCP-IP:
link: https://protegermipc.net/2013/09/30/como-calcular-una-mascara-de-subred-para-tcp-ip/ 

Aqui encontraras la forma de calcular subredes en Linux y Windows facilmente:                   
link: https://protegermipc.net/2017/11/22/como-calcular-subredes-en-linux-y-windows-facilmente/   

Tambien Podremos obtener los puertos abiertos de cada equipo de una subred mediante el 
siguiente comando:

comando utilizado: nmap <IP>*
ejemplo: nmap 192.168.1.*

Y poco más que decir, porque el resto de opciones siguen aplicando de igual forma que si se tratase de un 
escaneo convencional.
''')
        resp12()
    elif preg==2:
        Ip=input("Ingresar Ip: ")
        Msr=input("Ingresar Mascara de subred: ")
        os.system("nmap "+Ip+"/"+Msr)
        resp12()
        time.sleep(2)
    elif preg==3:
        banner()
    else:
        print("")
        print("Error ingrese una opcion valida(ej. '1' , '2' o '3') ")
        print("")
        time.sleep(2)
        resp12()  

#pregunta 13
def resp13():
   
    preg=int(input(Fore.LIGHTYELLOW_EX+'''
Ver información:
'''+
Fore.GREEN+'''1)'''+Style.RESET_ALL+Fore.BLUE+'''Si
'''+Style.RESET_ALL+
Fore.GREEN+'''2)'''+Style.RESET_ALL+Fore.BLUE+'''No(ejecutar comando)
'''+Style.RESET_ALL+
Fore.GREEN+'''3)'''+Style.RESET_ALL+Fore.BLUE+'''Regresar al menu principal
'''+Style.RESET_ALL+Fore.RED+
'''>>'''+Style.RESET_ALL))     
    if preg==1:
        print('''

Escaneo de toda la red con Nmap:

Si necesitamos descubrir equipos vivos (es decir, que nos digan “oye, aquí estoy”) en toda la red pero no 
queremos saber mucho sobre ellos, podemos lanzar un escaneo como el que sigue.   
Se nos mostrará el estado del host, su latencia (el tiempo que tarda en responder), su IP y su dirección MAC.     

comando utilizado: nmap -sP <IP>/<Máscara_de_red>        
ejemplo: nmap -sP 192.168.1.0/24    

        ''')     
        resp13()
    elif preg==2:
        Ip=input("Ingresar Ip: ")
        Msr=input("Ingresar Mascara de subred: ")        
        os.system("nmap -sP "+Ip/Msr)
        time.sleep(2)
        resp13()
    elif preg==3:
        banner()
    else:
        print("")
        print("Error ingrese una opcion valida(ej. '1' , '2' o '3') ")
        print("")
        time.sleep(2)
        resp13()         

#pregunta 14 
def resp14():
    
    preg=int(input('''
Ver información: 
1)Si
2)No(ejecutar comando)
3)Regresar al menu principal
>>'''))
    if preg==1:
        print('''

Escaneo de red con Nmap + puertos (rápido):

Con el siguiente comando podremos analizar toda una red o rango en busca de hosts. Se nos mostrarán los datos
del ejemplo anterior y además el estado de algunos de sus puertos (los más comunes).

comando utilizado: nmap -F/-f <IP>/<Máscara_de_Red>
ejemplo: nmap -F 192.168.1.0/24

F: la opción -F indica que el escaneo sea Fast (rápido). Es decir, no se analizarán tantos puertos como con un 
análisis corriente. Aquí se analizan los 100 puertos más comunes.

 ''')
        resp14()
    elif preg==2:
        Ip=input("Ingresar Ip: ")
        Msr=input("Ingresar Mascara de subred: ") 
        os.system("nmp -F "+Ip+"/"+Msr)
        time.sleep(2)
        resp14()
    elif preg==3:
        banner()
    else:
        print("")
        print("Error ingrese una opcion valida(ej. '1' , '2' o '3') ")
        print("")
        time.sleep(2)
        resp14()    

#pregunta 15
def resp15():
    
    preg=int(input(Fore.LIGHTYELLOW_EX+'''
Ver información:
'''+
Fore.GREEN+'''1)'''+Style.RESET_ALL+Fore.BLUE+'''Si
'''+Style.RESET_ALL+
Fore.GREEN+'''2)'''+Style.RESET_ALL+Fore.BLUE+'''No(ejecutar comando)
'''+Style.RESET_ALL+
Fore.GREEN+'''3)'''+Style.RESET_ALL+Fore.BLUE+'''Regresar al menu principal
'''+Style.RESET_ALL+Fore.RED+
'''>>'''+Style.RESET_ALL))
    if preg==1:
        print(''' 

Escaneo de red completa sigiloso con detección de SO:

Este tipo de escaneo se diferencia del anterior en que añade algunos datos adicionales, como son:

Tipo de dispositivo (device type): normalmente aparecerá “general purpose” o propósito general en ambientes 
domésticos.

Sistema operativo: intentará reconocer el sistema o kernel (en versiones Linux).

Distancia de red (network distance): se lanzará además una traza de red que nos indicará cuantos saltos nos
separan del dispositivo/red analizado.        
"""  """
comando utilizado: nmap -sS -O <IP>/<Máscara>   
ejemplo: nmap -sS -O 192.168.1.0/24        

Ss: técnica de escaneo SYN (otras opciones incluyen sT/sA/sW/sM)
O: detección de sistema operativo               
       
        ''')
        time.sleep(2)
        resp15()

    elif preg==2:
        Ip=input("Ingresar Ip: ")
        Msr=input("Ingresar Mascara de subred: ") 
        os.system("nmap -sS -O "+Ip+"/"+Msr)
        time.sleep(2)
        resp15()
    elif preg==3:
        banner()    
    else:
        print("")
        print("Error ingrese una opcion valida(ej. '1' , '2' o '3') ")
        print("")
        time.sleep(2)
        resp15()

#pregunta 16
def resp16():
    
    preg=int(input(Fore.LIGHTYELLOW_EX+'''
Ver información:
'''+
Fore.GREEN+'''1)'''+Style.RESET_ALL+Fore.BLUE+'''Si
'''+Style.RESET_ALL+
Fore.GREEN+'''2)'''+Style.RESET_ALL+Fore.BLUE+'''No(ejecutar comando)
'''+Style.RESET_ALL+
Fore.GREEN+'''3)'''+Style.RESET_ALL+Fore.BLUE+'''Regresar al menu principal
'''+Style.RESET_ALL+Fore.RED+
'''>>'''+Style.RESET_ALL))
    if preg==1:
        print('''

Usar scripts con Nmap:

Los scripts son útiles cuando buscamos información sobre diferentes tipos de ataque. Podemos utilizar un único 
script o incluso un conjunto de ellos (para ahorrar tiempo).

Un ejemplo sería el siguiente script, que busca ataques de tipo heartbleed:      
comando utilizado: nmap -sV -p 443 --script=ssl-heartbleed <IP>
ejemplo:nmap -sV -p 443 --script=ssl-heartbleed 192.168.43.1 

Para actualizar la base de datos de scripts de Nmap (actualmente en torno a 500) usaremos el comando:
comando utilizado: nmap --script-updatedb

Para visualizar los scripts disponibles, podemos usar el comando.
Kali linux: locate nse | grep script
Windows: nmap --script-help *

La opción anterior muestra todos los scripts de la base de datos. Para obtener información sobre uno en concreto usaremos:

comando utilizado: nmap –script-help=<nombre>

Los scripts nos permitirán realizar una gran cantidad de auditorías de seguridad de red y cosas más “interesantes”. 
Si nos tomamos en serio la seguridad de nuestro entorno, será de gran utilidad tomar contacto con estos scripts.

Mas informacion:
link: https://clibre.io/blog/por-secciones/hardening/item/452-scripts-en-nmap
       
        ''')
        time.sleep(2)
        resp16()

    elif preg==2:
        print("Actualizando base de datos de scripts././././.")
        os.system("sudo nmap --script-updatedb")
        clearConsole()
        os.system("nmap --script-updatedb")
        clearConsole()
        scrpt=input("Ingresar nombre del script: ")
        objetivo=input("Ingresar objetivo: ")
        puerto=input("Ingresar puerto: ")
        os.system("nmap -sV -p "+puerto+"--script="+scrpt+objetivo )
        time.sleep(2)
        resp16()
    elif preg==3:
        
        banner()
    else: 
        print("")
        print("Error ingrese una opcion valida(ej. '1' , '2' o '3') ")
        print("")
        time.sleep(2)
        resp16() 


#pregunta 17 
def resp17():
    
    preg=int(input(Fore.LIGHTYELLOW_EX+'''
Ver información:
'''+
Fore.GREEN+'''1)'''+Style.RESET_ALL+Fore.BLUE+'''Si
'''+Style.RESET_ALL+
Fore.GREEN+'''2)'''+Style.RESET_ALL+Fore.BLUE+'''No(ejecutar comando)
'''+Style.RESET_ALL+
Fore.GREEN+'''3)'''+Style.RESET_ALL+Fore.BLUE+'''Regresar al menu principal
'''+Style.RESET_ALL+Fore.RED+
'''>>'''+Style.RESET_ALL))
    if preg==1:
        print('''

Evitar el descubrimiento de hosts:

Finalmente dejo un truco que será de ayuda para no llamar la atención. Nmap normalmente lanza un descubrimiento 
de red con cada comando, aunque especifiquemos un puerto específico (por ejemplo: nmap -p 80 ejemplo.com).
Con el siguiente parámetro es posible evitarlo y asi levantaremos menos alarmas:  

comando utilizado: nmap -PN -p 80 ejemplo.com     
      
        ''')
        time.sleep(2)    
        resp17()
    elif preg==2:
        obj=input("ingresar objetivo: ")
        puerto=input("Ingresar puerto: ")
        os.system("nmap -PN -p "+puerto+" "+obj)
        time.sleep(2)
        resp17()
        
    elif preg==3:
        banner()
    else: 
        print("")
        print("Error ingrese una opcion valida(ej. '1' , '2' o '3') ")
        print("")
        time.sleep(2)
        resp17() 

#pregunta 18
def resp18():
   
    preg=int(input(Fore.LIGHTYELLOW_EX+'''
Ver información:
'''+
Fore.GREEN+'''1)'''+Style.RESET_ALL+Fore.BLUE+'''Si
'''+Style.RESET_ALL+
Fore.GREEN+'''2)'''+Style.RESET_ALL+Fore.BLUE+'''No(ejecutar comando)
'''+Style.RESET_ALL+
Fore.GREEN+'''3)'''+Style.RESET_ALL+Fore.BLUE+'''Regresar al menu principal
'''+Style.RESET_ALL+Fore.RED+
'''>>'''+Style.RESET_ALL))
    if preg==1:
        print('''
    
Escaneo desde un archivo:

Mediante una de las opciones que nos ofrece nmap, podremos realizar el escaneo de varios host o equipos desde 
un fichero en el que los tenemos almacenados. Muy útil si vamos tomando notas de varios equipos que queremos 
escanear y realizar dicho escaneo en un momento determinado (por ejemplo en un momento de máxima actividad o por 
el contrario en un momento donde la carga de trabajo sea mínima).        

comando utilizado: nmap –iL "nombre_del_archivo".txt
ejemplo: nmap –iL ips.txt       
           
        ''')
        time.sleep(2)
        resp18()
    elif preg==2:
        arch=input("Ingrese el nombre del archivo(incluido el '.txt'): ")
        os.system('nmap -iL '+arch)
        time.sleep(2)
        resp18()
    elif preg==3:
        banner()
    else: 
        print("")
        print("Error ingrese una opcion valida(ej. '1' , '2' o '3') ")
        print("")
        time.sleep(2)
        resp18() 

#pregunta 19 
def resp19():
   
    preg=int(input(Fore.LIGHTYELLOW_EX+'''
Ver información:
'''+
Fore.GREEN+'''1)'''+Style.RESET_ALL+Fore.BLUE+'''Si
'''+Style.RESET_ALL+
Fore.GREEN+'''2)'''+Style.RESET_ALL+Fore.BLUE+'''No(ejecutar comando)
'''+Style.RESET_ALL+
Fore.GREEN+'''3)'''+Style.RESET_ALL+Fore.BLUE+'''Regresar al menu principal
'''+Style.RESET_ALL+Fore.RED+
'''>>'''+Style.RESET_ALL))
    if preg==1:
        print('''

Escaneo Multiobjetivo:

Para recopilar información de varios objetivos a la vez sólo deberemos pasarle al comando 
dichos objetivos separados por espacios:   

comando utilizado: nmap <IP1> <IP2> <IP3>   
ejemplo: nmap 192.168.1.135 192.168.1.136 192.168.1.139  

        ''')
        resp19()
    elif preg==2:
        ips=""
        registro=input("Ingrese la cantidad de objetivos: ")
        for i in range(int(registro)):
            us=input(str(i+1)+") Ingresar objetivo: ")
            ips=str(ips)+" "+us+" "
        os.system('nmap '+ips)
        time.sleep(2)
        resp19()
    elif preg==3:
        banner()
    else: 
        print("")
        print("Error ingrese una opcion valida(ej. '1' , '2' o '3') ")
        print("")
        time.sleep(2)
        resp19()

def resp20():
    print(''' 

Nmap:

Cuando se trata de escoger las mejores herramientas de hacking o ciberseguridad, en el apartado 
de escaneo / inventariado de redes siempre hay una que destaca por encima del resto:nmap(mapeador de redes).
Nmap admite como valores para escaneo diferentes elementos: nombres de host (hostnames), direcciones
IP o redes completas, entre otros.
Esta navaja suiza de las redes y seguridad ofrece una variedad de tipos de análisis y opciones (incluida la de usar scripts)
que la convierte en preferible para muchos.

A continuación una muestra de los comandos que considero más útiles o quizá más demandados por los usuarios 
y administradores de seguridad o sistemas. Evidentemente no es una lista completa, echarás en falta muchos 
si conoces la herramienta. No olvidemos que esto es un script que busca servir de ayuda para principiantes.
   
    ''')
    time.sleep(2)
    input("Presiona 'Enter' para ir al menu principal.")
    banner()

#salir
def salir():
    exit()     







def banner():  
    clearConsole()                                     
    bans=int(input(Fore.YELLOW+'''                                      
███╗   ██╗███╗   ███╗ █████╗ ██████╗     ███████╗ ██████╗ ██████╗       
████╗  ██║████╗ ████║██╔══██╗██╔══██╗    ██╔════╝██╔═══██╗██╔══██╗      
██╔██╗ ██║██╔████╔██║███████║██████╔╝    █████╗  ██║   ██║██████╔╝      
██║╚██╗██║██║╚██╔╝██║██╔══██║██╔═══╝     ██╔══╝  ██║   ██║██╔══██╗      
██║ ╚████║██║ ╚═╝ ██║██║  ██║██║         ██║     ╚██████╔╝██║  ██║      
╚═╝  ╚═══╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝         ╚═╝      ╚═════╝ ╚═╝  ╚═╝      
                                                                        
██████╗ ███████╗ ██████╗ ██╗███╗   ██╗███╗   ██╗███████╗██████╗ ███████╗
██╔══██╗██╔════╝██╔════╝ ██║████╗  ██║████╗  ██║██╔════╝██╔══██╗██╔════╝
██████╔╝█████╗  ██║  ███╗██║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝███████╗
██╔══██╗██╔══╝  ██║   ██║██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗╚════██║
██████╔╝███████╗╚██████╔╝██║██║ ╚████║██║ ╚████║███████╗██║  ██║███████║
╚═════╝ ╚══════╝ ╚═════╝ ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚══════╝
'''+Fore.LIGHTMAGENTA_EX+
'''
by: b i y i v i

'''+Style.RESET_ALL+Fore.GREEN+Style.BRIGHT+
'''
   Elige una opcion: 

'''+Fore.BLUE + Style.BRIGHT+"   01)"+Style.RESET_ALL+Fore.RED+''' Escanear Hostname o IP
'''+Fore.BLUE + Style.BRIGHT+"   02)"+Style.RESET_ALL+Fore.RED+''' Escaneo de puertos TCP basico
'''+Fore.BLUE + Style.BRIGHT+"   03)"+Style.RESET_ALL+Fore.RED+''' Escanear un rango de IPs
'''+Fore.BLUE + Style.BRIGHT+"   04)"+Style.RESET_ALL+Fore.RED+''' Escanear puertos concretos o rangos de puertos
'''+Fore.BLUE + Style.BRIGHT+"   05)"+Style.RESET_ALL+Fore.RED+''' Escanear todos lo puertos
'''+Fore.BLUE + Style.BRIGHT+"   06)"+Style.RESET_ALL+Fore.RED+''' Lanzar un escaneo TCP SYN (opción por defecto)
'''+Fore.BLUE + Style.BRIGHT+"   07)"+Style.RESET_ALL+Fore.RED+''' Escaneo de sistema operativo
'''+Fore.BLUE + Style.BRIGHT+"   08)"+Style.RESET_ALL+Fore.RED+''' Escaneo de Sistema Operativo y servicios
'''+Fore.BLUE + Style.BRIGHT+"   09)"+Style.RESET_ALL+Fore.RED+''' Escaneo de servicios estandar 
'''+Fore.BLUE + Style.BRIGHT+"   10)"+Style.RESET_ALL+Fore.RED+''' Escaneo de servicios agresivo
'''+Fore.BLUE + Style.BRIGHT+"   11)"+Style.RESET_ALL+Fore.RED+''' Escaneo de servicios de banner ligero
'''+Fore.BLUE + Style.BRIGHT+"   12)"+Style.RESET_ALL+Fore.RED+''' Escaneo de una subred completa
'''+Fore.BLUE + Style.BRIGHT+"   13)"+Style.RESET_ALL+Fore.RED+''' Escaneo de toda la red (simple)
'''+Fore.BLUE + Style.BRIGHT+"   14)"+Style.RESET_ALL+Fore.RED+''' Escaneo de red + puertos (rápido)
'''+Fore.BLUE + Style.BRIGHT+"   15)"+Style.RESET_ALL+Fore.RED+''' Escaneo de red completa sigiloso con detección de SO
'''+Fore.BLUE + Style.BRIGHT+"   16)"+Style.RESET_ALL+Fore.RED+''' Usar scripts con Nmap
'''+Fore.BLUE + Style.BRIGHT+"   17)"+Style.RESET_ALL+Fore.RED+''' Evitar el descubrimiento de hosts
'''+Fore.BLUE + Style.BRIGHT+"   18)"+Style.RESET_ALL+Fore.RED+''' Escaneo desde un archivo
'''+Fore.BLUE + Style.BRIGHT+"   19)"+Style.RESET_ALL+Fore.RED+''' Escaneo Multiobjetivo
'''+Fore.BLUE + Style.BRIGHT+"   20)"+Style.RESET_ALL+Fore.RED+''' Nmap
'''+Fore.BLUE + Style.BRIGHT+"   21)"+Style.RESET_ALL+Fore.LIGHTRED_EX+''' Exit

    '''+Fore.RED+">>> "+Style.RESET_ALL))
    print("")

    if bans==1 :
        resp()
    elif bans==2:
        resp2()    
    elif bans==3:
        resp3() 
    elif bans==4:
        resp4()
    elif bans==5:
        resp5()            
    elif bans==6:
        resp6()                        
    elif bans==7:
        resp7()
    elif bans==8:
        resp8()
    elif bans==9:
        resp9()
    elif bans==10:
        resp10()
    elif bans==11:
        resp11()
    elif bans==12:
        resp12()
    elif bans==13:
        resp13()
    elif bans==14:
        resp14()
    elif bans==15:
        resp15()
    elif bans==16:
        resp16()
    elif bans==17:
        resp17()
    elif bans==18:
        resp18()
    elif bans==19:
        resp19()
    elif bans==20:
        resp20()
    elif bans==21:
        salir()
    else: 
        print("Error ingrese una opcion valida. ")
        time.sleep(2)
        banner()
banner()
