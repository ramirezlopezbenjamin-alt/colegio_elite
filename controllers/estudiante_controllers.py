from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.estudiante_model import EstudianteModel

estudiante_bp = Blueprint('estudiante', __name__, url_prefix='/estudiantes')

@estudiante_bp.route('/')
def index():
    estudiantes = EstudianteModel.obtener_todos()
    return render_template('estudiante/index.html', estudiantes=estudiantes)

@estudiante_bp.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        email = request.form['email']
        EstudianteModel.crear(nombre, apellido, email)
        flash('Estudiante registrado exitosamente.', 'success')
        return redirect(url_for('estudiante.index'))
    return render_template('estudiante/create.html')

@estudiante_bp.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        email = request.form['email']
        EstudianteModel.actualizar(id, nombre, apellido, email)
        flash('Datos del estudiante actualizados.', 'warning')
        return redirect(url_for('estudiante.index'))
    
    estudiante = EstudianteModel.obtener_por_id(id)
    return render_template('estudiante/editar.html', estudiante=estudiante)

@estudiante_bp.route('/eliminar/<int:id>', methods=['POST'])
def eliminar(id):
    EstudianteModel.eliminar(id)
    flash('Estudiante eliminado correctamente.', 'danger')
    return redirect(url_for('estudiante.index'))