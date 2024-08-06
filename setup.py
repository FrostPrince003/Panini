import setuptools

with open("README.md","r",encoding="utf-8") as f:
    long_description = f.read()
    
__version__ = "0.0.0"

REPO_NAME = "Panini"
AUTHOR_USER_NAME = "FrostPrince003"
SRC_REPO = "Panini"
AUTHOR_EMAIL = "kunjekarkartik@gmail.com"

setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small project for python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/" + AUTHOR_USER_NAME + "/" + REPO_NAME,
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}"
    },
    packages=setuptools.find_packages(where="src"),
    package_dir={"": "src"},
    )