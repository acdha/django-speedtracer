from distutils.core import setup
import os

setup(
    name='django-speedtracer',
    version='0.1.1',
    license='BSD',
    description="Profile your Django site using Google Chrome's SpeedTracer",
    long_description=open(os.path.join(os.path.dirname(__file__), "README.rst")).read(),
    author='Chris Adams',
    author_email='chris@improbable.org',
    url='http://github.com/acdha/django-speedtracer',
    include_package_data=True,
    zip_safe=False,
    packages=[
        'speedtracer',
    ],
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

