from django.http import HttpResponse
from django_user_agents.utils import get_user_agent

def index(request):
    # Detectar tipo de dispositivo
    user_agent = get_user_agent(request)
    is_mobile = user_agent.is_mobile
    is_tablet = user_agent.is_tablet

    if is_mobile:
        device_message = "¡Estás accediendo desde un dispositivo móvil!"
    elif is_tablet:
        device_message = "¡Estás accediendo desde una tablet!"
    else:
        device_message = "¡Estás accediendo desde una computadora!"

    return HttpResponse(f"""
    <!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Battlezone</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {{
            background-color: #214c68;
        }}

        .header {{
            background-image: url('/static/imagenes/fondo.jpg');
            background-size: cover;
            background-position: center center;
            height: 250px;
            display: flex;
            align-items: center;
            justify-content: center;
        }}

        .profile-img {{
            width: 150px;
            height: 150px;
            border-radius: 50%;
            border: 3px solid white;
        }}

        .profile-section {{
            text-align: center;
            margin-top: -75px;
            z-index: 1;
        }}

        .profile-section h2 {{
            color: white;
            font-size: 2.5rem;
            font-weight: bold;
            margin-top: 10px;
        }}

        .profile-section p {{
            color: white;
            font-size: 1.2rem;
        }}

        .tabs .nav-link.active {{
            color: white;
            background-color: #6c63ff;
        }}

        .tabs {{
            margin-top: 20px;
        }}

        .box {{
            background-color: #2b6cb0;
            border-radius: 10px;
            padding: 15px;
            margin-top: 20px;
        }}

        .card-title {{
            font-size: 1.3rem;
            color: white;
        }}

        .card-text {{
            color: white;
            font-size: 1rem;
        }}

        .qr-info-container {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-top: 30px;
        }}

        .qr-container2 {{
            flex: 1;
            display: flex;
            justify-content: center;
        }}

        .info-container {{
            flex: 1;
            text-align: left;
            padding-right: 20px;
        }}

        .qr-container img {{
            width: 350px;
            height: 350px;
        }}
                        
        .qr-container2 {{
            flex: 1;
            display: flex;
            justify-content: center;
            padding-top: 150px;
        }}
        .qr-container3 {{
            flex: 1;
            display: flex;
            justify-content: center;
            padding-top: 150px;
        }}
        .qr-container3 img {{
            width: 250px;
            height: 250px;
        }}
                        
        .qr-container2 img {{
            width: 200px;
            height: 200px;
        }}
                        
        .content-box {{
            background-color: #1e3d57;
            padding: 15px;
            border-radius: 10px;
            color: white;
            margin-bottom: 20px;
        }}

        .content-box h5 {{
            font-size: 1.5rem;
        }}

        .content-box p {{
            font-size: 1.2rem;
        }}

        .cta-box {{
            background-color: #214c68;
            padding: 15px;
            border-radius: 10px;
            color: white;
            text-align: center;
            margin-top: 20px;
        }}

        .cta-box h5 {{
            font-size: 1.5rem;
        }}

        body {{
            background-color: #183346;
            color: white; /* Para asegurar que el texto sea visible sobre el fondo oscuro */
        }}
        owo {{
Pa        }}  
    </style>
</head>
<body>
    <div class="header"></div>

    <div class="container mt-4">
        <!-- Profile Section -->
        <div class="profile-section">
            <img src="/static/imagenes/logo.png" alt="Foto de perfil" class="profile-img">
            <h2>Battle zone</h2>
            <p>La magia de los E-Sports al alcance de tu mano</p>
            <p>{device_message}</p> <!-- Aquí se muestra el mensaje dinámico -->
        </div>

        <!-- Navigation Tabs -->
        <hr></hr>

        <!-- Call to Action Box (Vamos a Jugar!!) -->
        <div class="cta-box">
            <h5>¿Que es Battlezone?</h5>
            <p>Battlezone es una aplicacion movil que esta disponible para todos los dispositivos , esta aplicacion te hara vivir experiencias inolvidables dandote una patada inicial en el mundo competitivo (E-Sports) ,ademas de poder obtener ganancias jugando , divirtiendote y compitiendo</p>
        </div>

        <!-- QR and Info Containers (flex layout) -->
        <div class="qr-info-container">
            <!-- Info Box -->
            <div class="info-container">
                <h1>Comienza a jugar </h1>
                <p>➤Valorant </p>
                <p>➤League Of legends </p>
                <p>➤Street Fighter </p>
                <p>➤Fortnite </p>
                        <hr></hr>

            </div>


{f"""
                    <!-- QR Code Box -->
            <div class="qr-container">
                 <h1>Escanea para jugar</h1>
                <img src="/static/imagenes/qr.png" alt="QR Code">

            </div>
        """ if device_message =="¡Estás accediendo desde una computadora!" else ""}


        </div>

{f"""
                    <!-- QR Code Box -->
            <div class="qr-container3">
                 <h1 class="owo">Haz click en el logo para descargar </h1>
              <a href="https://github.com/Chitowo/Battlezone">

                <img src="/static/imagenes/logoo.png" alt="QR Code">
  </a>

         <hr></hr>

         <hr></hr>

            </div>
        """ if device_message =="¡Estás accediendo desde un dispositivo móvil!" else ""}

{f"""
                    <!-- QR Code Box -->
            <div class="qr-container3">
                   <h1 class="owo">Haz click en el logo para descargar </h1>

             <a href="https://github.com/Chitowo/Battlezone">

                <img src="/static/imagenes/logoo.png" alt="QR Code">
 </a>

            </div>
        """ if device_message =="¡Estás accediendo desde una tablet!" else ""}

         <hr></hr>


        <!-- Discord Link -->
        <div class="qr-container2">
                         <h1 class="owo">Unete a Nuestro discord</h1>

            <a href="https://discord.gg/4CSkAbJrRH">
                <img src="/static/imagenes/discord.png" alt="Discord QR">
            </a>
        </div>
    </div>
    


</body>
</html>
    """)
