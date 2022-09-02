import setuptools

with open("README.md", "r", encoding="utf-8") as file:
    long_description = file.read()

setuptools.setup(
    name="pytools kit",
    version="1.0.0",
    author="KidCoderT",
    author_email="tejas75o25@gmail.com",
    description="Utils that help with system processes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/KidCoderT/pytool-kit",
    packages=setuptools.find_packages(),
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
