from setuptools import setup

setup(
    name='cheapbot',
    version='0.0.1',
    description='DNS Authenticator for Namecheap DNS',
    author='Ziad Hassanin',
    author_email='ziadmansour.4.9.2000@gmail.com',
    url='https://github.com/ZiadMansourM/cheapbot',
    package='cheapbot.py',
    install_requires=[
        'certbot',
    ],
    entry_points={
        'certbot.plugins': [
            'cheapbot = cheapbot:CheapBotAuthenticator',
        ],
    },
)
