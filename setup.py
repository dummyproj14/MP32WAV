import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="MP32Wav",
    version="0.0.1a",
    author="Bjorn Goriatcheff",
    author_email="bjorn.goriatcheff@gmail.com",
    description="Wrapper for pydub, multi file processing",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    include_package_data=True,
    package_data={'data':['data/default/*.txt'], },

    install_requires=['ffmpeg'],
    python_requires=">=3.6",
)

