from flask import Flask, redirect, url_for
from controllers.estudiante_controllers import estudiante_bp

app = Flask(__name__)

# Registrar el Blueprint (controlador) de estudiantes
app.register_blueprint(estudiante_bp)

@app.route('/')
def home():
    # Redirigir la raíz del sitio a la lista de estudiantes
    return redirect(url_for('estudiante.index'))

if __name__ == '__main__':
    app.run(debug=True)