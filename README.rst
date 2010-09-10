Django Speed Tracer
===================

Simple performance monitoring for Django using Google Chrome's Speed Tracer

Installation
------------

#. Download and install Speed Tracer: http://code.google.com/webtoolkit/speedtracer/get-started.html

#. Add ``"speedtracer"`` to your ``INSTALLED_APPS``

#. Add ``"speedtracer.middleware.SpeedTracerMiddleware"`` to the beginning of
   your ``MIDDLEWARE_CLASSES`` (this is important if you're also using projects like
   ``django-localeurl`` which alter normal URL routing)

#. Load your page inside Chrome with SpeedTracer enabled

#. Open SpeedTracer and expand the "Server Trace" in the page's detailed
   report which should look something like this:
   
   .. image:: http://farm5.static.flickr.com/4115/4815493734_4c20d6894f.jpg
   