from settings import INSTALLED_APPS, TEMPLATE_CONTEXT_PROCESSORS

TEMPLATE_CONTEXT_PROCESSORS += (

    # Required by allauth template tags
    "django.core.context_processors.request",

    # allauth specific context processors
    "allauth.account.context_processors.account",
    "allauth.socialaccount.context_processors.socialaccount",

)

AUTHENTICATION_BACKENDS = (

    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",

    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",

)

INSTALLED_APPS += (

    # The Django sites framework is required
    'django.contrib.sites',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # ... include the providers you want to enable:
    #'allauth.socialaccount.providers.amazon',
    #'allauth.socialaccount.providers.angellist',
    #'allauth.socialaccount.providers.bitbucket',
    # 'allauth.socialaccount.providers.bitly',
    # 'allauth.socialaccount.providers.dropbox',
    'allauth.socialaccount.providers.facebook',
    # 'allauth.socialaccount.providers.flickr',
    # 'allauth.socialaccount.providers.feedly',
    # 'allauth.socialaccount.providers.github',
    # 'allauth.socialaccount.providers.google',
    # 'allauth.socialaccount.providers.hubic',
    # 'allauth.socialaccount.providers.instagram',
    # 'allauth.socialaccount.providers.linkedin',
    # 'allauth.socialaccount.providers.linkedin_oauth2',
    # 'allauth.socialaccount.providers.openid',
    # 'allauth.socialaccount.providers.persona',
    # 'allauth.socialaccount.providers.soundcloud',
    # 'allauth.socialaccount.providers.stackexchange',
    # 'allauth.socialaccount.providers.tumblr',
    # 'allauth.socialaccount.providers.twitch',
    # 'allauth.socialaccount.providers.twitter',
    # 'allauth.socialaccount.providers.vimeo',
    # 'allauth.socialaccount.providers.vk',
    # 'allauth.socialaccount.providers.weibo',
    # 'allauth.socialaccount.providers.xing',

)

SITE_ID = 1

ACCOUNT_EMAIL_REQUIRED = True

SOCIALACCOUNT_PROVIDERS = \
    {'facebook':
       {'SCOPE': ['email'] , #, 'public_profile', 'user_friends', 'user_location'],
        'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
        'METHOD': 'oauth2',
        'LOCALE_FUNC': lambda request: 'en_US',
        #'VERIFIED_EMAIL': False
        }}

ACCOUNT_AUTHENTICATION_METHOD = "username_email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "none" # TODO need smtp setup before switching to optional
ACCOUNT_EMAIL_SUBJECT_PREFIX = "[myemail]"

