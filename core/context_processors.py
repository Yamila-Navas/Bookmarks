from decouple import config

def site_settings(request):
    return {
        "SITE_URL": config("SITE_URL")
    }