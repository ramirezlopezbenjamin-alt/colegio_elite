from flask import Flask, redirect, url_for
from controllers.estudiante_controllers import estudiante_bp


app = Flask(__name__)
app.secret_key = 'clave_secreta_colegio_elite'  # Necesaria para activar las alertas flash

# Registrar Blueprint
app.register_blueprint(estudiante_bp)

@app.route('/')
def home():
    return redirect(url_for('estudiante.index'))

if __name__ == '__main__':
    app.run(debug=True)