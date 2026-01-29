# 📌 Bookmarks – Social Website con Django

Es una aplicación social completa donde los usuarios pueden registrarse, seguir a otros usuarios, compartir imágenes, interactuar con contenido y ver actividad en tiempo real.

---

## 🚀 Funcionalidades principales

* 🔐 Autenticación de usuarios (login, logout, cambio y reseteo de contraseña)
* 👤 Registro de usuarios y perfiles extendidos
* 🖼️ Sistema de marcadores de imágenes (image bookmarking)
* ❤️ Relaciones *follow / unfollow* entre usuarios
* 📰 Feed de actividad (activity stream)
* ⚡ Acciones asíncronas con JavaScript (AJAX)
* 🧠 Optimización de QuerySets (`select_related`, `prefetch_related`)
* 🧮 Conteo de vistas y ranking de imágenes con **Redis**
* 🛠️ Señales de Django para desnormalizar contadores
* 🐞 Django Debug Toolbar para debugging

---

## 🧱 Tecnologías usadas

* **Python**
* **Django**
* **Redis**
* **PostgreSQL / SQLite** (según entorno)
* **JavaScript** (AJAX)
* **easy-thumbnails** (thumbnails de imágenes)
* **Pillow** (manejo de imágenes)

---

## ⚙️ Instalación y uso

### 1️⃣ Clonar el repositorio

```bash
git clone https://github.com/Yamila-Navas/Bookmarks.git
cd Bookmarks
```

### 2️⃣ Crear y activar entorno virtual

```bash
python -m venv env
source env/bin/activate
```

### 3️⃣ Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4️⃣ Migraciones

```bash
python manage.py migrate
```

### 5️⃣ Crear superusuario

```bash
python manage.py createsuperuser
```

### 6️⃣ Ejecutar Redis

```bash
redis-server
```

### 7️⃣ Ejecutar el servidor

```bash
python manage.py runserver
```

---

## 🧪 Características técnicas destacadas

* Uso de **ManyToMany con modelo intermedio** para followers
* **GenericForeignKey** para el stream de actividad
* **Signals** para mantener contadores consistentes
* **Redis Sorted Sets** para ranking de imágenes
* Separación clara de lógica (views, servicios, templates)

---

## 📚 Estado del proyecto

✔️ Proyecto funcional

---

## 🙌 Créditos

Proyecto desarrollado como parte del aprendizaje avanzado de Django.