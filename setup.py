
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='EasyTwitch',  
     version='0.1',
     author="JustFast",
     description="Making Twitch IRC easy",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/JustFast/EasyTwitch",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "Operating System :: OS Independent",
     ],
 )
