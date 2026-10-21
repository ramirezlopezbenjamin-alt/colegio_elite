from flask import Blueprint, render_template, request, redirect, url_for
from models.cursos_model import CursoModel

curso_bp = Blueprint('curso', __name__, url_prefix='/cursos')

# 1. Ruta para ver la lista de cursos (Read)
@curso_bp.route('/')
def index():
    cursos = CursoModel.obtener_todos()
    return render_template('curso/index.html', cursos=cursos)

# 2. Ruta para mostrar y procesar el formulario de creación (Create)
@curso_bp.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        nombre_curso = request.form['nombre_curso']
        nivel = request.form['nivel']
        id_sala = request.form['id_sala']
        CursoModel.crear(nombre_curso, nivel, id_sala)
        return redirect(url_for('curso.index'))
    return render_template('curso/create.html')

# 3. Ruta para editar un curso (Update)
@curso_bp.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    if request.method == 'POST':
        nombre_curso = request.form['nombre_curso']
        nivel = request.form['nivel']
        id_sala = request.form['id_sala']
        CursoModel.actualizar(id, nombre_curso, nivel, id_sala)
        return redirect(url_for('curso.index'))
    
    curso = CursoModel.obtener_por_id(id)
    return render_template('curso/editar.html', curso=curso)

# 4. Ruta para eliminar un curso (Delete)
@curso_bp.route('/eliminar/<int:id>', methods=['POST'])
def eliminar(id):
    CursoModel.eliminar(id)
    return redirect(url_for('curso.index'))