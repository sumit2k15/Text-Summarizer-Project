import setuptools

with open("README.md", "r",encoding="utf-8") as fh:
    long_description = fh.read()



__version__ = "0.0.0"

REPO_NAME = "Text-Summarizer-Project"
AUTHOR_USER_NAME = "sumit2k15"
SRC_REPO ="textSummarizer"
AUTHOR_EMAIL = "sumit8108@gmail.com"

setuptools.setup(
    name="SRC_REPO",
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email= AUTHOR_EMAIL,
    description="A simple python package for text summarization" ,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    packages=setuptools.find_packages(where="src"),
    package_dir={"": "src"}
)