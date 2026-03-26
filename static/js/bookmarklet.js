const siteUrl = (window.bookmarkletSettings?.siteUrl || '').replace(/\/$/, '');
const styleUrl = siteUrl + '/static/css/bookmarklet.css';
const minWidth = 50;
const minHeight = 50;

if (!siteUrl) {
  throw new Error('Bookmarklet misconfigured: missing siteUrl');
}

if (!document.querySelector(`link[data-bookmarklet-css="${styleUrl}"]`)) {
  const head = document.getElementsByTagName('head')[0];
  const link = document.createElement('link');
  link.rel = 'stylesheet';
  link.type = 'text/css';
  link.href = styleUrl + '?r=' + Math.floor(Math.random() * 9999999999999999);
  link.dataset.bookmarkletCss = styleUrl;
  head.appendChild(link);
}

if (!document.getElementById('bookmarklet')) {
  const body = document.getElementsByTagName('body')[0];
  const boxHtml = `
      <div id="bookmarklet">
          <a href="#" id="close">&times;</a>
          <h1>Select an image to bookmark:</h1>
          <div class="images"></div>
      </div>`;
  body.insertAdjacentHTML('beforeend', boxHtml);
}

function hasValidImageExtension(url) {
  const cleanUrl = url.split('?')[0].toLowerCase();
  return ['.jpg', '.jpeg', '.png'].some(extension => cleanUrl.endsWith(extension));
}


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
  bookmarklet.querySelector('#close').onclick = function (event) {
    event.preventDefault();
    bookmarklet.style.display = 'none';
  };

  // Buscar todas las imágenes del DOM y filtrar extensiones válidas
  const images = document.querySelectorAll('img');

  // Recorrer todas las imágenes encontradas
  images.forEach(image => {

    // Filtrar solo imágenes grandes
    // minWidth y minHeight deben existir previamente
    const imageUrl = image.currentSrc || image.src;

    if (
      hasValidImageExtension(imageUrl) &&
      image.naturalWidth >= minWidth &&
      image.naturalHeight >= minHeight
    ) {
      // Crear una nueva imagen
      const imageFound = document.createElement('img');

      // Copiar la URL de la imagen original
      imageFound.src = imageUrl;

      // Agregar la imagen al panel del bookmarklet
      imagesFound.append(imageFound);
    }
  });

    // select image event
    imagesFound.querySelectorAll('img').forEach(image => {
    image.addEventListener('click', function(event){
        const imageSelected = event.target;
        bookmarklet.style.display = 'none';
        window.open(siteUrl + '/images/create/?url='
                + encodeURIComponent(imageSelected.src)
                + '&title='
                + encodeURIComponent(document.title),
                '_blank');
    })
  })
}

window.bookmarkletLaunch = bookmarkletLaunch;

// Ejecutar el bookmarklet
bookmarkletLaunch();
