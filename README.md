# *Proyecto Introducción a sistemas*
Se realizó un software de encriptado y decriptado de archivos de texto para sistemas UNIX mediante una interfaz de linea de comandos. Los modos de encriptado y decriptado son Cesaro, Vigenere, Vernam.

### *Breve introducción teorica a los modos*:


### Método de Cesar
Para este método se utilizó una variacíon al método clásico que requiere una transformación afín del estilo
$$T:\mathbb{Z}_p\to\mathbb{Z}_p$$
donde $\mathbb{Z}_p$ son los enteros módulo $p\in\mathbb{N}$ y  $T(x) = ax+b$. Para poder garantizar el decifrado del cifrado resultante es necesario que $mcd(a,p) = 1$ para asegurar que $T$ tenga inversa. 

### Método de Vigenere
Es una variación del método de Cesar anterior donde $a$ y $b$ no son fijos sino son una lista de elementos (no necesariamente del mismo tamaño) donde cada elemento de $a$ es primo relativo con $p$. Así si $a = \{a_1, a_2\}$ y $b = \{b_1,b_2,b_3\}$ y queriendo cifrar la parabra *ferrocarril* tendríamos la siguiente distribución:



| $F$ | $a_1$ | $b_1$ |
|---|-----|-----|
| $E$ | $a_2$ | $b_2$ |
| $R$ | $a_1$ | $b_3$ |
| $R$ | $a_2$ | $b_1$ |
| $O$ | $a_1$ | $b_2$ |
| $C$ | $a_2$ | $b_3$ |
| $A$ | $a_1$ | $b_1$ |
| $R$ | $a_2$ | $b_2$ |
| $R$ | $a_1$ | $b_3$ |
| $I$ | $a_2$ | $b_1$ |
| $L$ | $a_1$ | $b_2$ |



### Método de Vernam

Por último, el método de Vernam ocupa la misma transformación de Cesar sin embargo para cada carácter genera $a$ y $b$ de forma pseudoaleatoria, lo que lo lleva a ser un método muy seguro (ya que no tiene patrones probabiísticos) sin embargo es un método lento.

## Descripción del programa
El programá está realizado en Python 3.8.10, por lo que cualquier sistema UNIX con esa versón o superior de Python 3 no debería tener problemas. Las librerías no nativas utilizadas son las siguientes click, sympy, pyinstaller, cryptography. 

## Instalación

* Actualice el sistema 
  - debian derivados: sudo apt update
  - arch-linux derivados sudo pacman -Syu
* Para instalar las tependencias ejecute en terminal
  - pip3 install click sympy pyinstaller cryptography
  - debian: sudo apt install git
  - arch: sudo pacman -S git
* Diríjase a la carpeta an la que desee descargar los scripts y ejecute en terminal
   - git clone https://github.com/Yamileche/ProyectoIS.git && cd ProyectoIS
* En ../ProyectoIS ejecutar
  - pyinstaller --onefile main.py
  Lo anterior creará un ejecutable y archivos derivados
* De la siguiente liga https://correoipn-my.sharepoint.com/:f:/g/personal/mvelazquezm1400_alumno_ipn_mx/Eugpo2a0ZcdGuiRWQbYro7IButmcBpilndOf1aNG65FBRA?e=Ctcf9a descargue el archivo primes.txt en ../ProyectoIS/dist
  
## Forma de empleo
* Abra una terminal y dirijase a la carpeta ../ProyectoIS/dist
* Ejecute *./main* para ver las opciones 
  * decrypt  (Decrypt mode)
  * encrypt  (Encrypt mode)
  * rank     (Random keys)
  * ranp     (Random prime)

* encrypt:
  * cesaro: 
    * El principio pedirá ingresar un directorio en el cual trabajar. En dado caso que no se desee trabajar en un directorio para dar las rutas relativas simplemente oprima *enter*
    * Luego pedirá ingresar los valores de las claves *a* y *b* y el módulo *p*.
    * A continuación se ingresará el texto a encriptar, puede ser por medio de consola o por un archivo de texto. En caso de que se desee ingresar por un archivo de texto sólo basta con ingresar el nombre del archivo (sin extension) en dado caso que se haya escogido un directorio de trabajo.
    * Luego se proceserá a encriptar el archivo y se pedirá el modo de entrega del texto encriptado, ya sea por archivo de texto (si se tiene un directorio de trabajo basta con poner el nombre del archivo sin extension) o la ruta del mismo (en dado caso que no se tenca directorio de trabajo) 
  * vigenere:
    * Se siguen los mismos pasos que en Cesaro, la única diferencia es que al momento de pedir las claves pueden ser ingresadas por consola o por un archivo de texto, el módulo debe ingresarse por consola.
  * vernam:
    * Debilo a la naturaleza de este algoritmo, siguiendo pasos muy similares a los métodos anteriores, sólo basta ingresar el archivo a encriptar y regresará el archivo encriptado y las claves *a* y *b* ya sea por consola o por archivo de texto, el módulo debe ingresarse por consola.
* decrypt: Debido a que son los algoritmos inversos a los álgoritmos anteriores para los tres algorítmos se pedirán las claves, el módulo y el texto a encriptar. En el algoritmo de *cesaro* no se puede ingresar las claves por archivo de texto mientras que en los otros dos algoritmos es pasible tanto por consola como por archivo de texto. Además, también se tiene la opción de escoger un directorio de trabajo siguiendo los pasos ya mencionados.
* rank: Hace referencia a random keys (claves aleatorias). Genera un número *n* de claves dependiendo de un módulo *p*. Las claves resultantes no tendrás factores primos con común con el módulo *p*
* ranp: Hace referencia a random prime (primo aleatorio), que en efecto selecciona un primo *pseudo aleatorio* del archivo de primos

**Ejemplos**: En una terminal dirijase a *../ProyectoIS/dist* e ingrese
* *./main encrypt --cesaro*
* *./main encrypt --vigenere*
* *./main encrypt --vernam*
* *./main decrypt --cesaro*
* *./main decrypt --vigenere*
* *./main decrypt --vernam*
* *./main rank*
* *./main ranp*
 