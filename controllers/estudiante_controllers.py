from flask import Blueprint, render_template, request, redirect, url_for
from models.estudiante_model import EstudianteModel

# Crear un Blueprint para agrupar las rutas de estudiantes
estudiante_bp = Blueprint('estudiante', __name__, url_prefix='/estudiantes')

# 1. Ruta para ver la lista de estudiantes (Read)
@estudiante_bp.route('/')
def index():
    estudiantes = EstudianteModel.obtener_todos()
    return render_template('estudiante/index.html', estudiantes=estudiantes)

# 2. Ruta para mostrar y procesar el formulario de creación (Create)
@estudiante_bp.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        email = request.form['email']
        EstudianteModel.crear(nombre, apellido, email)
        return redirect(url_for('estudiante.index'))
    return render_template('estudiante/create.html')

# 3. Ruta para editar un estudiante (Update)
@estudiante_bp.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        email = request.form['email']
        EstudianteModel.actualizar(id, nombre, apellido, email)
        return redirect(url_for('estudiante.index'))
    
    estudiante = EstudianteModel.obtener_por_id(id)
    return render_template('estudiante/editar.html', estudiante=estudiante)

# 4. Ruta para eliminar un estudiante (Delete)
@estudiante_bp.route('/eliminar/<int:id>', methods=['POST'])
def eliminar(id):
    EstudianteModel.eliminar(id)
    return redirect(url_for('estudiante.index'))