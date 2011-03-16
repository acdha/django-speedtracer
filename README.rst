Django Speed Tracer
===================

Simple performance monitoring for Django using Google Chrome's Speed Tracer

Notes
-----

Chrome Dev channel has not been stable with the Speed Tracer extension. If you
don't see the server trace results or anything in the request/response headers
you are probably running into this issue:

http://code.google.com/p/speedtracer/issues/detail?id=28

Installation
------------

#. Download and install Speed Tracer:

    http://code.google.com/webtoolkit/speedtracer/get-started.html

#. Add ``"speedtracer"`` to your ``INSTALLED_APPS``

#. Add ``"speedtracer.middleware.SpeedTracerMiddleware"`` to the beginning of
   your ``MIDDLEWARE_CLASSES`` (this is important if you're also using projects like
   ``django-localeurl`` which alter normal URL routing)

#. Load your page inside Chrome with SpeedTracer enabled

#. Open SpeedTracer and expand the "Server Trace" in the page's detailed
   report which should look something like this:

   .. image:: http://farm5.static.flickr.com/4115/4815493734_4c20d6894f.jpg

Example
-------

There is a simple example project available in example_project which can
be used to test the UI:

#. Create a virtualenv
#. Install django
#. Change into example_project and run ``manage.py runserver``
