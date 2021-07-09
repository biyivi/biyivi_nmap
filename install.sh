echo "Iniciando  instalacion..."
sleep 2 
pkg install python -y
clear
pip install colorama
clear
pip install tqdm
clear
echo "La instalacion se ha completado.."
var1="1"

echo "Instalar nmap"
echo "1)Si"
echo "2)No"
read -p ">> " resp1
if [ "$resp1" == "$var1" ]
then
apt install nmap -y
clear
fi
echo "Iniciar script"
echo "1) Si"
echo "2) Salir"
read -p ">> " resp
if [ "$resp" == "$var1" ]
then
python nmap_bgnnrs.py
else
echo "Para iniciar el scripit debe escribir: python nmap_bgnnrs.py"
echo ":D"
fi
