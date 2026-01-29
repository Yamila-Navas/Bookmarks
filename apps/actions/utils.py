from django.contrib.contenttypes.models import ContentType
import datetime
from django.utils import timezone
from .models import Action


def create_action(user, verb, target=None):
    '''
    Solo registro la acción si no se repitió en el último minuto
    evita spam
    evita feeds duplicados
    protege la base de datos
    '''
    now = timezone.now()
    last_minute = now - datetime.timedelta(seconds=60)

    # acciones similares del último minuto:
    similar_actions = Action.objects.filter(user_id=user.id, verb=verb, created__gte=last_minute )

    # si hay un target, filtrar también por él:
    if target:
        target_ct = ContentType.objects.get_for_model(target)
        similar_actions = similar_actions.filter(target_ct=target_ct, target_id=target.id)

    # si no hay acciones similares, crear una nueva:
    if not similar_actions:
        action = Action(user=user, verb=verb, target=target)
        action.save()
        return True
    return False