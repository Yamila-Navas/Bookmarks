/* 
Carga el bookmarklet una sola vez y lo ejecuta:

Si el bookmarklet todavía no está cargado:
- Descarga el archivo bookmarklet.js desde tu servidor
- Lo inyecta en la página
- Marca que ya está cargado

Si ya estaba cargado:
- No lo vuelve a descargar
- Solo lo ejecuta otra vez

Para qué sirve?
- Para poder actualizar el código cuando quieras
- Para evitar cargarlo dos veces
- Para que el bookmarklet funcione en cualquier página
*/


const SITE_URL = 'https://mysite.com:8000/';

(function(){
  if(!window.bookmarklet) {
    bookmarklet_js = document.body.appendChild(document.createElement('script'));
    bookmarklet_js.src = SITE_URL + '/static/js/bookmarklet.js?r='+Math.floor(Math.random()*9999999999999999);
    window.bookmarklet = true;
  }
  else {
    bookmarkletLaunch();
  }
})();