# Constants for the template views
SITE_CONFIG = {
    'COMPANY_NAME': "Save the World",
    'COMPANY_PHONE': "555-332333",
    'COMPANY_EMAIL': "save.the.world@fake.savetheworld.com",
    'COMPANY_TWITTER': "@savetheworld.fake",
    'COMPANY_FACEBOOK': "facebook.com"
}

# Exposes the constants to the context processor so it becomes available to all templates
def site_config(request):
    return SITE_CONFIG
    