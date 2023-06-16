import setuptools

with open("README.md", "r", encoding = "utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "Text-Summarization"
AUTHOR_USER_NAME = "aditipraveen"
SRC_REPO = "text_summarization"
AUTHOR_EMAIL = "aditipraveen10@gmail.com"


setuptools.setup(
    name = SRC_REPO,
    version = __version__,
    author = AUTHOR_USER_NAME,
    author_email = AUTHOR_EMAIL,
    description = "Text summarization project",
    long_description = long_description,
    long_description_content = "text/markdown",
    url = f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    project_urls = {
        "Bug_Tracker" : f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",   
    },
    package_dir = {"" : "src"},
    packages = setuptools.find_packages(where = "src")
)