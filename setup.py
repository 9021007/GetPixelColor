from setuptools import setup, find_packages
import sys
readme = open('README.md').read()

setup(
    name='GetPixelColor',
    version='0.1.3',    
    description='A cross-platform python library for getting the color of a given pixel on screen.',
    long_description=readme,
    long_description_content_type='text/markdown',
    url='https://github.com/Bobrobot1/GetPixelColor',
    author='Bobrobot1',
    author_email='bobrobot@zoho.com',
    license='MIT',
    packages=['getpixelcolor'],
    install_requires=[
                    'Pillow',
                    'numpy',
                    'pyautogui',
                    'pyobjc; platform_system == "darwin"',
                    'pyobjc-core; platform_system == "darwin"',
                    'pasteboard; platform_system == "darwin"',
                    'win32api; platform_system == "Windows"',
                    ],
    platforms=['Windows', 'Linux', 'Mac OS X'],
    

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',  
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',        
        'Programming Language :: Python :: 3'
    ],
)
