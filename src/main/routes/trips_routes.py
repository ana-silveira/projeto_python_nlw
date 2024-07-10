from flask import jsonify, Blueprint # O Blueprint vai deixar os nomes mais interessantes e bonitos

trips_routes_bp = Blueprint("trip_routes", __name__) #Todas as nossas rotas serão criadas com essa Blueprint

@trips_routes_bp.route("/trips", methods = {"POST"})
def create_trip():
    return jsonify({"Ola": "mundo"}), 200

# Pra saber que essa rota existe, precisei cadastrar essa Blueprint no meu servidor!, No server.py