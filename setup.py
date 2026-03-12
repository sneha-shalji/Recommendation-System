from setuptools import setup, find_packages


with open("README.md","r",encoding="utf-8") as f:
    long_description = f.read()

REPO_NAME = "Recommendation-ystem"    
AUTHOR_USERNAME = "sneha-shalji"
SRC_REPO = "book_recommeder"
LIST_OF_REQUIREMENTS = []



setup(name=SRC_REPO,
      version="0.0.1",
      author="SNEHA SHALJI",
      description=" Small local packages for ML Based Book Recommedations",
      long_description = long_description,
      long_description_content_type = "text/markdown",
      url= "https://github.com/sneha-shalji/Recommendation-System",
      packages=find_packages(),
      license="MIT",
      python_requires=">3.7",
      install_requires = LIST_OF_REQUIREMENTS

      
      )

