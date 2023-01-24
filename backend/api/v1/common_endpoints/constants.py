from backend.core.constants import AppStringEnum


class APIResponseMessageTemplate(AppStringEnum):
    """Template messages for API response"""
    BACKEND_MODE_INFO = 'App work mode'
    VERSION_INFO = 'App vesrion'
    CONFIGURATION_INFO = 'Insensitive config information'
