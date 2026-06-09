Sistema de Control de Acceso Basado en Roles (RBAC) con Django
Descripción

Este proyecto implementa un sistema de Control de Acceso Basado en Roles (RBAC) desarrollado con Django. Su objetivo es gestionar el acceso a los recursos de una aplicación web según el rol asignado a cada usuario.

El sistema incorpora autenticación de usuarios, gestión de roles y paneles personalizados para cada perfil, permitiendo aplicar principios fundamentales de seguridad informática como autenticación, autorización y mínimo privilegio.

Objetivos
Implementar un sistema de autenticación de usuarios.
Aplicar el modelo de Control de Acceso Basado en Roles (RBAC).
Restringir el acceso a funcionalidades según el rol del usuario.
Gestionar usuarios y permisos desde una interfaz administrativa.
Comprender conceptos de seguridad relacionados con autenticación y autorización.
Roles Implementados
Administrador (Admin)
Acceso total al sistema.
Creación y gestión de usuarios.
Asignación de roles.
Administración de permisos.
Docente (Teacher)
Acceso al panel docente.
Gestión de actividades académicas.
Consulta de estudiantes y materias asignadas.
Registro y consulta de calificaciones.
Estudiante (Student)
Acceso al panel estudiantil.
Consulta de materias inscritas.
Visualización de tareas y calificaciones.
Acceso a información personal.
Características del Sistema
Inicio de sesión seguro.
Gestión de sesiones de usuario.
Control de acceso basado en roles.
Dashboards personalizados para cada rol.
Restricción de vistas mediante decoradores personalizados.
Administración de usuarios desde el panel administrativo.
Arquitectura modular y escalable.
Tecnologías Utilizadas
Python 3
Django
SQLite
HTML5
CSS3
JavaScript