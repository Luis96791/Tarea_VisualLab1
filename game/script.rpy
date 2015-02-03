##      SOPORTE USADO:  THE QUESTION GAME
## La identación es obligatoria...

## La imagen del menu principal esta programada en las options.rpy
## En el apartado de Mas Perzonalizaciones....

# You can place the script of your game in this file.
# - Puedes colocar el 'script' de tu juego en este archivo.

# Declare images below this line, using the image statement.
# - Declara imágenes bajo esta línea, usando 'image' como
#   en el ejemplo.
# eg. image eileen happy = "eileen_happy.png"

## Se declaran todas las imagenes que se van a usar en el juego...

image Roblito = "Screen.png"
image eg blanco1 = "Blanco1.jpg"
image eg Foco = "foco.jpg"
image eg Foco1 = "foco1.jpg"
image eg paisaje = "paisaje2.png"
image eg atardecer = "Noche.png"
image eg Lluvia = "Lluvia.gif"
image eg Neblina = "Neblina.png"
image eg negro = "ImageBlack.jpg"
image eg Pulmon = "Pulmon.png"
image eg Aire1 = "aire1.jpg"
image eg Carretera = "Carretera1.jpg"
image eg ContAire1 = "ContAire1.jpg"
image eg Aire_Puro = "Aire_Puro.jpg"
image eg Agua1 = "ContAgua.gif"
image eg AguaCont2 = "AguaCont2.jpg"
image eg AguaCont3 = "AguaCont3.jpg"
image eg agua_pura = "agua_pura.jpg"

## Se declaran las imagenes que se van a utilizar encima de otras imagenes
## de preferencia .PNG

image Carro1 = "Carro1.png"
image Carro2 = "Carro2.png"
image arbolPNG = "Prueba2.png"
image roblito = "Roblito2.png"
image Roblito_Lado = "Roblito_Lado.png"
image GOTA = "G.png"
image Texto = "Texto.png"

# Declare characters used by this game.
# - Declara los personajes usados en el juego como en el 
#   ejemplo.
#define s = Character('Roblito', color="#c8ffc8")
#define m = Character('Cedrito', color="#c8c8ff")

# The game starts here.
# - El juego comienza aquí.
label start:
    ##La musica inicia luego de ejecutado el label start.
    play music "InEstambul.ogg" 
    ## Show se utiliza para mostrar una imagen sin fondo encima de un fondo.
    ## at center Nos da los parametros de la imagen puede ser: center, left, right.
    show Roblito at center
    ## Los comentarios que apareceran en la parte inferior de cada pantalla...
    "Hola... soy roblito y te quiero hablar sobre el daño que estas
     provocando al medio ambiente..."
    "Ultimamente nos hemos estado preguntando de ¿Que piensas tu respecto
     a la contaminacion y destruccion de nuestro medio ambiente?"
    
    ## scene declara una nueva escena la escena anterior es reemplazada
    scene eg Foco
    ## with dá un efecto a la entrada de la nueva imagen utilizé: fade y dissolve
    with fade
    "En esta ocasión tendre el placer de presentarte a un amigo"
    
    scene eg Foco1
    with fade
    "El es...                                          
     Cedrito"
    "Cuentales Cedrito ¿Como es que los seres humanos
    han afectado el medio ambiente?"
    
    scene eg paisaje
    with dissolve
    "Muy bien... Nuestro ecosistema solía ser el ecosistema más limpio
     puro y perfecto que podía existir..."
    "Hasta que un dia se le ocurrio a los humanos sacar provecho de 
     nuestros recursos..."
    
    scene eg atardecer
    with dissolve
    "Yo solía disfrutar mis noches bajo el sombrió y obscuro bosque
     tambien recuerdo la brisa nocturna surcando mis abundantes
     ramas..."
    
    scene eg Lluvia
    with dissolve
    "Recuerdo tambien mis dias en aquellos frondosos valles disfrutando de la
     lluvía invernal..."
    
    scene eg Neblina
    with dissolve
    "Mis mañanas en las frescas y nubladas montañas tropicales..."
    
    scene eg negro
    "Todo era maravilloso...
     Hasta que vino el hombre y comenzo a emplear su mano destructora 
     sobre todos nuestros bosques, rios, lagos, mares y hasta el aire mismo
     contaminaron con esos inventos de automoviles, maquinas a vapor e industrialización..."
    "El severo golpe de la Revolución Industrial que impactó a los seres humanos
     con su forma de dinero facíl pero sin darse cuenta del tremendo daño que causaban
     al ecosistema"
    "La única esperanza de vida del ser humano comenzaba a ser destruida..."
    
    scene eg Pulmon
    with dissolve
    "Elije un tema que te dejarán un pequeño concepto del daño que causas al medio ambiente..."
    
    ##El menú se presenta siempre que se requiera tomar una decisión
    menu:
        "Contaminación del Agua":
        ##"Contaminacion del agua" hace referencia a un boton
            jump agua
        ## jump agua me abre el label agua y ejecuta su contenido
        "Contaminación del Aire":
            
            jump aire
            
        "Salir":
            jump exit
            ##jump exit me devuelve al menu principal

## este label se ejecuta solo si se toma la opcion aire
label aire:
    scene eg Aire1
    with dissolve
    show arbolPNG at right
    show roblito at left
    "Cedrito:  Ves Roblito... Sobre eso estoy hablando, el humo de esas chimineas
     es un verdadero contaminante, se dispersa por el aire y de ahi se
     forman esas lluvias acidas que tanto daño hacen a la naturaleza y
     a los mismos seres humanos..."
    
    scene eg Carretera
    with dissolve
    show Carro1
    hide Carro1
    "El humo negro está compuesto, en promedio, por un 60 a 80 por ciento de macro- y micropartículas 
     que incluyen el humo negro..." 
    
    show Carro2
    "...a lo que se le suman cantidades variables de monóxido de carbono (CO), 
     dióxido de carbono (CO2), dióxido de azufre o anhídrido sulfuroso (SO2), óxidos de nitrógeno (NOX), 
     compuestos de plomo (Pb) e hidrocarburos aromáticos, entre otros."
    #Comentarios tomados de http://www.abc.com.py/articulos/contaminacion-por-humo-negro-372140.html
    
    scene eg ContAire1
    with dissolve
    "El mejor remedio a la contaminación de aire es basar toda nuestra vida en energías  limpias y renovables. 
     También es importante el control de las emisiones de gases por parte de las autoridades para 
     fomentar el uso de fuentes alternativas."
    
    show Roblito_Lado at left
    "El aire contaminado afecta tanto a países desarrollados como los que están sumidos en la pobreza."
    #Comentarios tomados de https://www.inspiraction.org/cambio-climatico/contaminacion/contaminacion-del-aire
    
    scene eg blanco1
    with fade
    show Texto
    ##ejecuta los comentarios de esa escena
    ##play music "My_movie.ogg"
    ""
    
    scene eg Pulmon
    ##Nuevamente muestra el menu del game para que me saqué del game hasta que 
    ##escoja la opcion salir...
    menu:
        "Contaminación del Agua":

            jump agua
            
        "Contaminación del Aire":
            
            jump aire
            
        "Salir":
            jump exit

## este label se ejecuta si es tomada la opcion agua...
label agua:
    scene eg Agua1
    with dissolve
    "La contaminación del Agua tambien es un problema con pocas soluciones veamos
     mas adelante algunas causas de la contaminación del agua y algunos efectos..."
    
    scene eg AguaCont2
    with dissolve
    show arbolPNG at right
    "La contaminación del agua es conocida desde la antigüedad. En Roma eran 
     frecuentes los envenenamientos provocados por el plomo de las tuberías que 
     transportaban el agua..."
    "En las ciudades medievales eran, habitualmente, sucias y pestilentes 
     y provocaban serios y extendidos problemas de salud que se fueron agravando cada vez más. 
     En la actualidad, es alarmante la constante pérdida de agua potable."
    
    scene eg AguaCont3
    with dissolve
    "Si bien las naciones industrializadas han tenido bastante éxito en el control de 
     la contaminación proveniente de industrias, siguen teniendo problemas con la escorrentía 
     en las tierras de cultivos y con las aguas que fluyen de los centros urbanos cargadas con 
     todos tipos de elementos."
    # Comentarios tomados de: http://www.ecojoven.com/tres/05/aguas.html
    
    scene eg agua_pura
    with dissolve
    show GOTA at left
    "El hombre, es el principal causante de la contaminación del agua, ya que  la eliminación 
     de residuos líquidos, domésticos e industriales, así como desperdicios sólidos como la basura, 
     en los ríos y otros cuerpos de agua, trae como consecuencia su inutilización. "
    "Cuidemos el agua... Cooperemos con la NO contaminacion del agua; en un futuro cercano tendremos
     agua limpia, pura y saludable..."
    # Comentarios tomados de : http://salvarelplaneta.blogia.com/2006/112905-la-contaminacion-del-agua.php
    scene eg Pulmon
    with dissolve    
    menu:
        "Contaminación del Agua":

            jump agua
            
        "Contaminación del Aire":
            
            jump aire
            
        "Salir":
            jump exit
label exit:
    scene eg Aire_Puro
    with dissolve
    show arbolPNG at left
    show roblito at right
    "..: Comenzemos a trabajar juntos por un ambiente puro y limpio..."
    scene negro
    return
##      La identaci{on es obligatoria
##      SOPORTE USADO:  THE QUESTION GAME
