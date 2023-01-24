from setuptools import setup


version = '0.0.1'

setup(
    name='project-base',
    version=version,
    description='FastAPI app common modules',
    classifiers=['Programming Language :: Python :: 3.11'],
    author='istrebitel',
    author_email='istrebitel.3.12@gmail.com',
    include_package_data=True,
    install_requires=[
        'alembic~=1.9.2',
        'fastapi~=0.89.1',
        'Jinja2~=3.1.2',
        'psycopg2-binary~=2.9.5',
        'pydantic[email]~=1.10.4',
        'SQLAlchemy~=1.4.46',
        'uvicorn~=0.20.0',
    ],
    extras_require={
        'code-quality': ['flake8~=6.0.0', 'mypy~=0.991'],
    },
    packages=[],
    python_requires=">=3.10",
    keywords='FastApiApp',
)
