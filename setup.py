import setuptools

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name="pycovid_india",
    version="0.0.1",
    author="T.THAVASI GTI",
    license="MIT",
    author_email="ganeshanthavasigti1032000@gmail.com",
    description="Indian COVID-19 Vaccine and Cases Status Information",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/THAVASIGTI/india_covid.git",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3',
)