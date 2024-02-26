import setuptools

with open("README.md",'r') as f:
    long_description= f.read()

__version__="0.0.0"


REPO_NAME="smartphonespriceprediction"
AUTHOR_USER_NAME="Aklesh",
SRC_REPO="smartphonespriceprediction"
AUTHOR_EMAIL="yaklesh802@gmail.com"
setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description= "A small python package for ml app",
    long_description=long_description,

    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    projects_url={"Bug Tracker":f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"

    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)
