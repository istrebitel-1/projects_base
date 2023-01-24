import os


env_variables = {
    'BACKEND_CORS_ORIGINS': '["http://localhost:8080"]',

    'APP_MODE': 'LOCAL',
    'APP_CONTAINERIZED': 'false',

    'APP_LOG_LEVEL': 'DEBUG',
    'APP_LOG_PATH': 'logs',

    'METADATA_POSTGRES_HOST': 'localhost',
    'METADATA_POSTGRES_PORT': '5430',
    'METADATA_POSTGRES_DATABASE': 'APP',
    'METADATA_POSTGRES_USERNAME': 'postgres',
    'METADATA_POSTGRES_PASSWORD': 'postgres',

    'PGTZ': 'UTC',

    'JWT_ACCESS_TOKEN_SECRET': 'LOCAL_SECRET_TOKEN',
    'JWT_ACCESS_TOKEN_EXPIRE_MINUTES': 7 * 24 * 60,
}


def apply_local_env():
    for var_key, var_val in env_variables.items():
        if os.getenv(var_key) is None:
            os.environ[var_key] = str(var_val)
