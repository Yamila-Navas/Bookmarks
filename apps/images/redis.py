from django.conf import settings
import redis
from .models import Image


r = redis.Redis(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT,
    db=settings.REDIS_DB
)


def get_total_views(user_id, image_id):
    # Total numero de vistas de una imgen con Redis
    user_key = f'image:{image_id}:viewed_by'
    views_key = f'image:{image_id}:views'
    is_new_view = r.sadd(user_key, user_id)
    if is_new_view:
        r.incr(views_key)
    total_views = int(r.get(views_key) or 0)

    # Ranking de imagenes mas vistas con Redis:
    r.zincrby('image_ranking', 1, image_id)
    return total_views


def image_ranking():
    # Desde Redis los IDs de las imágenes más vistas ordenados por score (vistas), de mayor a menor:
    image_ranking = r.zrange('image_ranking', 0 , 9 , desc=True)
    image_ranking_ids = [int(id) for id in image_ranking]

    # Busco esas imágenes en la base de datos, luego reordeno respetando el orden de image_ranking_ids:
    most_viewed = list(Image.objects.filter(id__in=image_ranking_ids))
    most_viewed.sort(key=lambda  x : image_ranking_ids.index(x.id))
    return  most_viewed


        
