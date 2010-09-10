from distutils.core import setup

setup(
    name='django-speedtracer',
    version='0.1',
    license='BSD',
    description="Profile your Django site using Google Chrome's SpeedTracer",
    author='Chris Adams',
    author_email='chris@improbable.org',
    url='http://github.com/acdha/django-speedtracer',
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

