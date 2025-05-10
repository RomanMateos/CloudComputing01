# Manual para Alumnos: Trabajo con Fork, Branches y Pull Requests en GitHub

---

## 📅 Introducción
En esta guía aprenderás a:
- Hacer un **fork** de un repositorio de clase.
- Crear una **carpeta** con tu nombre y apellido.
- Crear un **archivo Python** que imprima algo.
- Crear una **rama (branch)** para tu trabajo.
- **Hacer push** de tus cambios.
- Crear un **Pull Request (PR)** para que el profesor revise tu código.
- **Actualizar tu fork** si el repositorio original cambió.

---

## 🔄 Paso 1: Realizar un Fork del Repositorio
1. Ingresa al repositorio del profesor (ejemplo: `https://github.com/Bastyprof/CloudComputing01.git`).
2. Haz clic en el botón **Fork** (esquina superior derecha).
3. Se creará una copia en tu cuenta de GitHub.

---

## 🔄 Paso 2: Clonar tu Fork a tu Computadora

```bash
# Clona tu propio fork
git clone https://github.com/Bastyprof/CloudComputing01.git
cd big-data-clase
```

---

## 🔄 Paso 3: Crear una Nueva Rama (Branch)

```bash
# Cambia a la rama principal y actualiza
git checkout main
git pull origin main

# Crea una nueva rama para tu tarea
git checkout -b nombre-apellido-tarea
```
**Ejemplo:**
```bash
git checkout -b perez-juan-tarea1
```

---

## 🔄 Paso 4: Crear Carpeta y Archivo Python

1. Crea una carpeta con tu nombre y apellido (sin espacios).
2. Dentro de la carpeta, crea un archivo Python que imprima algo.

**Ejemplo de comandos:**
```bash
mkdir perez-juan
cd perez-juan
echo 'print("Hola, soy Juan Pérez")' > saludo.py
```

---

## 🔄 Paso 5: Hacer Commit y Push de tus Cambios

```bash
# Verifica los cambios
git status

# Agrega los archivos nuevos
git add .

# Crea un commit
git commit -m "Agrego carpeta y saludo en Python"

# Sube tu rama al repositorio remoto
git push origin nombre-apellido-tarea
```

---

## 🔄 Paso 6: Crear un Pull Request (PR)

1. Ve a tu repositorio en GitHub.
2. GitHub mostrará un botón: **"Compare & pull request"**.
3. Haz clic, completa:
   - **Título**: "Agrego carpeta y saludo - Nombre Apellido"
   - **Comentario**: Breve explicación de lo que hiciste.
4. Asigna al **profesor** como revisor del PR.

---

## 💡 Paso 7: Resolver Problemas de Actualización del Fork

Si el repositorio original del profesor tiene cambios nuevos:

### Agrega el repositorio original como "upstream"
```bash
git remote add upstream https://github.com/Bastyprof/CloudComputing01.git
```

### Actualiza tu main con cambios del profesor
```bash
git fetch upstream
git checkout main
git merge upstream/main
```

### Actualiza tu repositorio en GitHub
```bash
git push origin main
```

**Nota:** Siempre crea nuevas ramas a partir de tu main actualizado.

---

## 📈 Buenas Prácticas
- Siempre crea una rama nueva para cada tarea.
- Nombra correctamente tus carpetas y archivos.
- Asegúrate de que tu código funcione antes de hacer pull request.
- Mantén tu fork actualizado con el repositorio del profesor.

---

## 🚀 ¡Listo!
Con estos pasos, tu flujo de trabajo en Git y GitHub será profesional y ordenado.
