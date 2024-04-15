from models.db import Database
from models.cursos import Cursos
from models.inscripciones import Inscripciones
from models.inscripciones import ProgresoLecciones

class AdminBackend:
    def __init__(self, user):
        self.user = user
        self.cursos_model = Cursos()
        self.inscripciones_model = Inscripciones()
        self.progreso_lecciones_modelmo = ProgresoLecciones()

    def tiene_permiso(self, permiso):
        return permiso in self.user.permisos

    def ver_todos_los_cursos(self):
        if self.tiene_permiso("ver_cursos"):
            return self.cursos_model.get_all_cursos()
        else:
            raise PermissionError("No tienes permiso para ver todos los cursos")

    def ver_detalle_curso(self, curso_id):
        if self.tiene_permiso("ver_cursos"):
            return self.cursos_model.obtener_curso_por_id(curso_id)
        else:
            raise PermissionError("No tienes permiso para ver detalles de cursos")

    def ver_inscripciones_de_usuario(self, usuario_id):
        if self.tiene_permiso("ver_inscripciones"):
            return self.inscripciones_model.get_inscripciones_by_usuario(usuario_id)
        else:
            raise PermissionError("No tienes permiso para ver las inscripciones de usuarios")

    def ver_progreso_de_lecciones_de_usuario(self, usuario_id):
        if self.tiene_permiso("ver_progreso_lecciones"):
            return self.progreso_lecciones_model.get_progresos_by_usuario(usuario_id)
        else:
            raise PermissionError("No tienes permiso para ver el progreso de lecciones de usuarios")

    def eliminar_inscripcion(self, inscripcion_id):
        if self.tiene_permiso("eliminar_inscripciones"):
            return self.inscripciones_model.eliminar_inscripcion_por_id(inscripcion_id)
        else:
            raise PermissionError("No tienes permiso para eliminar inscripciones")
