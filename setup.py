import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="brain-games-pkg-Amon-Ra", # Replace with your own username
    version="0.7.0",
    author="Amon_Ra",
    author_email="mighty.python777@gmail.com",
    description="A small package that will train your mind",
    long_description="Please don`t",
    long_description_content_type="text/markdown",
    url="https://github.com/GDNeural/python-project-lvl1.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3"
    ],
    python_requires='>=3.6'
    )