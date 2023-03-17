from setuptools import find_packages, setup


setup(
    name='larousse',
    version='0.0.1',
    packages=find_packages('larousse'),

    install_requires=
    [
        'beautifulsoup4==4.10.0', 
        'requests==2.27.1',
        'lxml==4.7.1'
    ],
    entry_points = {
        'console_scripts': [
            'larousse=larousse.app:main',
        ]
    }
)