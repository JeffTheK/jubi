from setuptools import setup

setup(
    name = "jubi",
    version = "1.0.0",
    description = "ls clone",
    author = "JeffTheK",
    url = "https://github.com/JeffTheK/jubi",
    packages = ["jubi"],
    entry_points = {
        'console_scripts': [
            'jubi = jubi.__main__:main'
        ]
    },
)