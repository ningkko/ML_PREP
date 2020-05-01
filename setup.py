import setuptools

with open("README.md", "r") as fh:
    readme = fh.read()

requires = ['nltk',
            'numpy',
            'matplotlib',
            'pandas',
            'scipy']
setuptools.setup(
    name="Conceptual dependency",
    version="0.0.1",
    author="Neneka",
    author_email="makiasagawa@gmail.com",
    description="Something I wrote for the MARGIE text generator efficiency test ",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/ningkko/ConceptualDependency",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=requires)