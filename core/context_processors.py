from decouple import config

def site_settings(request):
    site_url = config("SITE_URL", default="").rstrip("/")
    return {
        "SITE_URL": site_url
    }
