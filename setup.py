import setuptools

with open("README.md","r",encoding="utf-g") as f:
  long_discription=f.read()

__version__="0.0.0"
REPO_NAME ="deep-learning-tutorial"
AUTHOR_USER_NAME = "dhivyabharath-30"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "dhivyabharath2005@gmail.com"

setuptools.setup(
  name=SRC_REPO,
  version=__version__,
  author=AUTHOR_USER_NAME,
  author_email=AUTHOR_EMAIL,
  description="A small python package for CNN app",
  Long_description=long_discription,
  long_description_content="text/markdown",
  url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
  project_url={
    "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
  },
  package_dir={"":"src"},
  packages=setuptools.find_packages(where="src")
)