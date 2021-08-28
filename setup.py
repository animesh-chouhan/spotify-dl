import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="spotify-dl",
    version="0.0.1",
    author="Animesh Singh Chouhan",
    author_email="animeshsingh.iitkgp@gmail.com",
    description="Download your Spotify playlists and songs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/animesh-chouhan/spotify-dl",
    project_urls={
        "Bug Tracker": "https://github.com/animesh-chouhan/spotify-dl/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    entry_points={
        "console_scripts": ["spotify-dl=spotify-dl.cli:main"]
    },
)
