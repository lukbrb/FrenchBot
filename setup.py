from setuptools import find_packages, setup


setup(
    name='frenchbot',
    version='0.0.1',
    packages=find_packages('scraper'),

    install_requires=
    [
        'beautifulsoup4==4.10.0', 
        'requests==2.27.1'
    ],
    entry_points = {
        'console_scripts': [
            'frenchbot=scraper.app:main',
        ]
    }
)