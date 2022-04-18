from setuptools import setup

with open("README.md", encoding="utf-8") as f:
    readme = f.read()

setup(
    name="feeds2pdf",
    version="0.1.9",
    description="Convert RSS/Atom feeds into a single e-reader compatible PDF",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Alexander Senier",
    author_email="mail@senier.net",
    url="https://github.com/senier/feeds2pdf",
    license="Apache License 2.0",
    python_requires=">=3.7",
    install_requires=[
        "feedparser",
        "pandoc",
        "readability-lxml",
        "html2text",
    ],
    scripts=["feeds2pdf"],
)
