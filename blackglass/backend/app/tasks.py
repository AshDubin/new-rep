from .celery_app import celery_app
from .services.hibp import check_email_breach
from .services.vehicle import lookup_plate
from .services.image import analyze_image
from .services.location import lookup_location
from .services.breach import search_breaches
from .services.social import github_profile, reddit_profile, instagram_profile


@celery_app.task
def hibp_email_search(email: str):
    return check_email_breach(email)


@celery_app.task
def vehicle_lookup_task(plate: str):
    return lookup_plate(plate)


@celery_app.task
def image_analysis_task(url: str):
    return analyze_image(url)


@celery_app.task
def location_lookup_task(handle: str):
    return lookup_location(handle)


@celery_app.task
def breach_search_task(query: str):
    return search_breaches(query)


@celery_app.task
def social_lookup_task(username: str):
    return {
        "github": github_profile(username),
        "reddit": reddit_profile(username),
        "instagram": instagram_profile(username),
    }
