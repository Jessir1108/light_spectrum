import streamlit as st
from PIL import Image

# Crear un sidebar con 6 opciones
st.sidebar.title("Menú")
st.markdown("***German David Florez Hamburger - Semana de la ciencia***")


option = st.sidebar.selectbox(
    "Selecciona una opción",
    ["Inicío", "Ondas de radio", "Microondas", "Infrarrojo", "Luz visible", "Ultravioleta", "Rayos X", "Rayos Gamma"]
)

# Contenido principal de la aplicación
if option == "Inicío":
    st.title("Espectro Electromagnético")

    st.markdown("El espectro electromagnético es un rango de frecuencias, longitudes de onda y energías de fotones que abarcan frecuencias desde menos de 1 hercio hasta más de 1025 Hz, correspondientes a longitudes de onda que van desde unos pocos kilómetros hasta una fracción del tamaño de un núcleo atómico en el espectro de ondas electromagnéticas. Generalmente, en el vacío, las ondas electromagnéticas tienden a viajar a velocidades similares a la de la luz. Sin embargo, lo hacen en una amplia gama de longitudes de onda, frecuencias y energías de fotones.")

    # Carga la imagen de presentación
    image = Image.open("Espectro Luz dreamstime.jpg")
    st.image(image, use_column_width=True, caption='Espectro electromagnético')

elif option == "Ondas de radio":
    st.title("Ondas de radio ")

    st.markdown("Las ondas de radio tienen las longitudes de onda más largas del espectro electromagnético. Varían desde la longitud de una pelota de fútbol hasta más grandes que nuestro planeta. Heinrich Hertz demostró la existencia de las ondas de radio a finales de la década de 1880. Usó un vía de chispas unida a una bobina de inducción y una vía de chispas separada en una antena receptora. Cuando la antena receptora captaba las ondas creadas por las chispas del transmisor de la bobina, las chispas también saltaban su espacio. Hertz demostró en sus experimentos que estas señales poseían todas las propiedades de las ondas electromagnéticas.")

    # Carga la imagen de presentación
    image = Image.open("radio.png")
    st.image(image, use_column_width=True, caption='Sistema de transmisión y recepción de un radio')

elif option == "Microondas":
    st.title("Microondas")

    st.markdown("Es posible que esté familiarizado con las imágenes de microondas, ya que se usan en las noticias meteorológicas de la televisión e incluso puede usar microondas para cocinar sus alimentos. Los hornos microondas funcionan utilizando microondas de unos 12 centímetros de largo para forzar la rotación de las moléculas de agua y grasa de los alimentos. La interacción de estas moléculas que sufren rotación forzada genera calor y la comida se cocina.")

    st.markdown("Las microondas son una porción o banda que se encuentra en el extremo de frecuencia más alta del espectro de radio, pero comúnmente se distinguen de las ondas de radio debido a las tecnologías utilizadas para acceder a ellas. ")

    # Carga la imagen de presentación
    image = Image.open("microondas.jpg")
    st.image(image, use_column_width=True, caption='Fondo cosmico de microondas')
    # Agrega contenido para la Microondas

elif option == "Infrarrojo":
    st.title("Infrarrojo")

    st.markdown("Las ondas infrarrojas, o luz infrarroja, forman parte del espectro electromagnético. La gente encuentra ondas infrarrojas todos los días; el ojo humano no puede verlo, pero los humanos pueden detectarlo en forma de calor.")

    st.markdown("Un control remoto utiliza ondas de luz más allá del espectro de luz visible (ondas de luz infrarroja) para cambiar los canales de su televisor. Esta región del espectro se divide en infrarrojo cercano, medio y lejano. Los científicos terrestres se refieren a la región de 8 a 15 micrones (μm) como infrarrojo térmico, ya que estas longitudes de onda son las mejores para estudiar la energía térmica de onda larga que irradia nuestro planeta.")

    # Carga la imagen de presentación
    image = Image.open("human-infrared.jpg")
    st.image(image, use_column_width=True, caption='Cámara infrarroja enfocando a una persona (Temperatura en Fahrenheit)')

elif option == "Luz visible":
    st.title("Luz visible")
    # Agrega contenido para la Luz visible

    st.markdown("El espectro de luz visible es el segmento del espectro electromagnético que el ojo humano puede ver. Más simplemente, este rango de longitudes de onda se llama luz visible. Normalmente, el ojo humano puede detectar longitudes de onda de 380 a 700 nanómetros.")
    
    st.markdown( "Toda la radiación electromagnética es luz, pero sólo podemos ver una pequeña porción de esta radiación: la porción que llamamos luz visible. Las células en forma de cono de nuestros ojos actúan como receptores sintonizados con las longitudes de onda de esta estrecha banda del espectro. Otras porciones del espectro tienen longitudes de onda demasiado grandes o demasiado pequeñas y energéticas para las limitaciones biológicas de nuestra percepción.")
    
    st.markdown("A medida que todo el espectro de luz visible viaja a través de un prisma, las longitudes de onda se separan en los colores del arco iris porque cada color tiene una longitud de onda diferente. El violeta tiene la longitud de onda más corta, alrededor de 380 nanómetros, y el rojo tiene la longitud de onda más larga, alrededor de 700 nanómetros.")

    # Carga la imagen de presentación
    image = Image.open("paisaje-multicolor.jpg")
    st.image(image, use_column_width=True, caption='Paisaje multicolor')

elif option == "Ultravioleta":
    st.title("Ultravioleta")

    st.markdown("La luz ultravioleta (UV) tiene longitudes de onda más cortas que la luz visible. Aunque las ondas ultravioleta son invisibles para el ojo humano, algunos insectos, como los abejorros, pueden verlas. Esto es similar a cómo un perro puede oír el sonido de un silbido justo fuera del alcance auditivo de los humanos.")

    st.header("Luz ultravioleta de nuestro sol")

    st.markdown("El Sol es una fuente de todo el espectro de radiación ultravioleta, que comúnmente se subdivide en UV-A, UV-B y UV-C. Estas son las clasificaciones más utilizadas en las ciencias de la Tierra. Los rayos UV-C son los más dañinos y nuestra atmósfera los absorbe casi por completo. Los rayos UV-B son los rayos dañinos que causan quemaduras solares. La exposición a los rayos UV-B aumenta el riesgo de daño al ADN y otros daños celulares en los organismos vivos. Afortunadamente, alrededor del 95 por ciento de los rayos UV-B son absorbidos por el ozono de la atmósfera terrestre.")

    # Carga la imagen de presentación
    image = Image.open("LuzUltravioleta.jpg")
    st.image(image, use_column_width=True, caption='Bombillo de luz ultravioleta')

elif option == "Rayos X":
    st.title("Rayos X")

    st.markdown("Los rayos X tienen mucha más energía y longitudes de onda mucho más cortas que la luz ultravioleta, y los científicos suelen referirse a los rayos X en términos de su energía más que de su longitud de onda. Esto se debe en parte a que los rayos X tienen longitudes de onda muy pequeñas, entre 0,03 y 3 nanómetros, tan pequeñas que algunos rayos X no son más grandes que un solo átomo de muchos elementos.")

    st.header("Descubrimiento de los rayos X")

    st.markdown("Los rayos X fueron observados y documentados por primera vez en 1895 por el científico alemán Wilhelm Conrad Roentgen. Descubrió que disparar corrientes de rayos X a través de brazos y manos creaba imágenes detalladas de los huesos del interior. Cuando le toman una radiografía, se coloca una película sensible a los rayos X en un lado de su cuerpo y los rayos X se disparan a través de usted. Debido a que los huesos son densos y absorben más rayos X que la piel, las sombras de los huesos quedan en la película de rayos X mientras que la piel parece transparente.")

    # Carga la imagen de presentación
    image = Image.open("Xray_share.jpg")
    st.image(image, use_column_width=True, caption='Rayos X en el pecho de una persona')

elif option == "Rayos Gamma":
    st.title("Rayos Gamma")

    st.markdown("Los rayos gamma tienen las longitudes de onda más pequeñas y la mayor energía de cualquier onda en el espectro electromagnético. Son producidos por los objetos más calientes y energéticos del universo, como estrellas de neutrones y púlsares, explosiones de supernovas y regiones alrededor de agujeros negros. En la Tierra, las ondas gamma son generadas por explosiones nucleares, rayos y la actividad menos dramática de la desintegración radiactiva.")

    st.header("Detección de los rayos Gamma")

    st.markdown("A diferencia de la luz óptica y los rayos X, los espejos no pueden capturar ni reflejar los rayos gamma. Las longitudes de onda de los rayos gamma son tan cortas que pueden atravesar el espacio dentro de los átomos de un detector. Los detectores de rayos gamma suelen contener bloques de cristal densamente empaquetados. A medida que los rayos gamma pasan, chocan con los electrones del cristal. Este proceso se llama dispersión Compton, en el que un rayo gamma incide sobre un electrón y pierde energía, similar a lo que sucede cuando una bola blanca golpea una bola ocho. Estas colisiones crean partículas cargadas que el sensor puede detectar.")

    # Carga la imagen de presentación
    image = Image.open("gamma.jpg")
    st.image(image, use_column_width=True, caption='Dispersión de rayos gamma por explosión de agujero negro')