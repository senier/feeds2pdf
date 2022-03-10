from setuptools import setup

with open("README.md", encoding="utf-8") as f:
    readme = f.read()

setup(
    name="rss2pdf",
    version="0.1.0",
    description="Convert RSS feed into e-reader compatible PDF",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Alexander Senier",
    author_email="mail@senier.net",
    url="https://github.com/senier/rss2pdf",
    license="Apache License 2.0",
    python_requires=">=3.7",
    install_requires=[
        "pandoc",
        "readability-lxml",
        "html2text",
    ],
    scripts=["rss2pdf"],
)
