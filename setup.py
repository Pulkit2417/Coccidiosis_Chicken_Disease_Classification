import setuptools

with open('README.md', 'r', encoding='utf-8') as file:
    long_description = file.read()


__version__ = "0.0.0"

REPO_NAME = "Coccidiosis_Chicken_Disease_Classification"
AUTHOR_USERNAME = "pulkit2417"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "forwebsurfingonly1@gmail.com"

setuptools.setup(
    name = SRC_REPO,
    version = __version__,
    author = AUTHOR_USERNAME,
    author_email = AUTHOR_EMAIL,
    description = "A small python package for cnn app",
    Long_description = long_description,
    Long_description_content = "text/markdown",
    url = f"https://github.com/{AUTHOR_USERNAME}/{REPO_NAME}",
    project_urls = {
        "Bug_Tracker": f"https://github.com/{AUTHOR_USERNAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)



