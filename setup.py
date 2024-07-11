import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME ="ShortHand-AI"
AUTHOR = "KamauWaData"
SRC_REPO = "ShortHand-AI"
AUTHOR_EMAIL = "kaharafredrick@gmail.com"

setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description="A simple python package for NLP app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR}/{SRC_REPO}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)