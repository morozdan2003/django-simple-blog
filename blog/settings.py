### django-simple-blog settings

## Bootstrap section

# Use offline version of Bootstrap instead of CDN
# True - use Bootstrap dist from static files
# False - use Bootstrap dist from CDN
USE_OFFLINE_BOOTSTRAP = False

# Online Bootstrap location (needed when OFFLINE_BOOTSTRAP is False)
ONLINE_BOOTSTRAP_LOCATION = 'https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist'

# Location of offline Bootstrap distro (relative to STATIC_URL)
OFFLINE_BOOTSTRAP_LOCATION = 'blog/bootstrap'