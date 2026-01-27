const siteUrl = '//127.0.0.1:8000/';
const styleUrl = siteUrl + 'static/css/bookmarklet.css';
const minWidth = 250;
const minHeight = 250;

// load CSS
var head = document.getElementsByTagName('head')[0];
var link = document.createElement('link');
link.rel = 'stylesheet';
link.type = 'text/css';
link.href = styleUrl + '?r=' + Math.floor(Math.random()*9999999999999999);
head.appendChild(link);

// load HTML
var body = document.getElementsByTagName('body')[0];
boxHtml = `
    <div id="bookmarklet">
        <a href="#" id="close">&times;</a>
        <h1>Select an image to bookmark:</h1>
        <div class="images"></div>
    </div>`;
body.innerHTML += boxHtml;


/**
 * Lanza el bookmarklet:
 * - Muestra un panel flotante
 * - Busca imágenes grandes en la página
 * - Las copia dentro del panel
 */
function bookmarkletLaunch() {

  // Obtener el contenedor principal del bookmarklet
  const bookmarklet = document.getElementById('bookmarklet');

  // Contenedor donde se van a mostrar las imágenes encontradas
  const imagesFound = bookmarklet.querySelector('.images');

  // Limpiar imágenes anteriores (por si se ejecuta más de una vez)
  imagesFound.innerHTML = '';

  // Mostrar el bookmarklet (antes estaba oculto)
  bookmarklet.style.display = 'block';

  // Botón de cerrar: oculta el bookmarklet al hacer click
  bookmarklet.querySelector('#close')
    .addEventListener('click', function () {
      bookmarklet.style.display = 'none';
    });

  // Buscar todas las imágenes JPG y PNG del DOM
  const images = document.querySelectorAll(
    'img[src$=".jpg"], img[src$=".jpeg"], img[src$=".png"]'
  );

  // Recorrer todas las imágenes encontradas
  images.forEach(image => {

    // Filtrar solo imágenes grandes
    // minWidth y minHeight deben existir previamente
    if (
      image.naturalWidth >= minWidth &&
      image.naturalHeight >= minHeight
    ) {
      // Crear una nueva imagen
      const imageFound = document.createElement('img');

      // Copiar la URL de la imagen original
      imageFound.src = image.src;

      // Agregar la imagen al panel del bookmarklet
      imagesFound.append(imageFound);
    }
  });

    // select image event
    imagesFound.querySelectorAll('img').forEach(image => {
    image.addEventListener('click', function(event){
        imageSelected = event.target;
        bookmarklet.style.display = 'none';
        window.open(siteUrl + 'images/create/?url='
                + encodeURIComponent(imageSelected.src)
                + '&title='
                + encodeURIComponent(document.title),
                '_blank');
    })
  })
}

// Ejecutar el bookmarklet
bookmarkletLaunch();
