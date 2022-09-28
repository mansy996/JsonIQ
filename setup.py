from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()


setup(
    name="jsoniq",
    version='0.1',
    py_modules=['jsoniq'],
    description="Query over Json file",
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: '
        'Python Modules',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
    author='Ahmed Mansy',
    author_email='ahmed.mansy996@gmail.com',
    license='MIT',
    url="",
    keywords=['Python', 'plugin'],
    include_package_data=True,
    zip_safe=False,
    setup_requires=['setuptools>=38.6.0'],
    readme="README.md",
)