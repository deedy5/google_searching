from setuptools import setup
from google_searching import __version__

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="google_searching",
    version=__version__,
    author="deedy5",
    author_email="deedy-ru@ya.ru",
    description="Scraping google search results",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/deedy5/google_searching",
    license="MIT",
    py_modules=["google_searching"],
    install_requires=["requests>=2.26.0", "lxml>=4.6.3"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Internet :: WWW/HTTP :: Indexing/Search",
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    python_requires=">=3.6",
    zip_safe=False,
)
