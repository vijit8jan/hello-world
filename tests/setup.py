from setuptools import setup, find_packages

setup(
    name="hello_world_app",
    version="0.1",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'hello-world=hello_world.main:main',
        ],
    },
)
