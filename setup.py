# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='uikit_editor',
    version='0.0.1',
    description='uikit_editor provides integration for UiKit htmleditor with Django',
    long_description=open('README.rst').read(),

    author='Alex Vakhitov',
    author_email='alex.vakhitov@gmail.com',
    license="Simplified BSD",
    url='https://github.com/smidth/django-uikit-editor',

    packages=['uikit_editor'],
    include_package_data=True,
    install_requires=['Django', 'setuptools'],

    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
)
