from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()


setup(
    name='jsoniq',
    version='0.1.1',
    license='MIT',
    description="Query over Json file",
    long_description_content_type='text/markdown',
    long_description=long_description,
    url='https://github.com/mansy996/JsonIQ',
    author='Ahmed Mansy',
    author_email='ahmed.mansy996@gmail.com',
    python_requires='>=3.6',
    classifiers = [
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    keywords=['Python', 'plugin'],
    include_package_data=True,
    zip_safe=False,
    setup_requires=['setuptools>=38.6.0'],
    readme = 'README.md',
)