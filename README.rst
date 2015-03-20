django-tagconstants
===================

Define constants in your settings file, that are then made available in
your templates.

Installation
============

From the command line:

::

    pip install django-tagconstants

Add tagconstants to your installed apps:

.. code:: python

    INSTALLED_APPS = (
        ...
        'tagconstants',
        ...
    )

Create a ``TAG_CONSTANTS`` dictionary in your ``settings.py`` file:

.. code:: python

    TAG_CONSTANTS = {}

Usage
=====

For security purposes, ``tagconstants`` is designed so that you create a
whitelist of variables to make available in your templates. For more
information see the **Design and Security** section.

To use a constant in your templates, first add the constant to your
``TAG_CONSTANTS`` setting:

.. code:: python

    TAG_CONSTANTS = {
        'CONSTANT': 'SOME STRING',
    }

Then in your templates, you can recall these constants with the
``{% constant ... %}`` template tag:

.. code:: html

    {% load tagconstants %}

    {% constant "CONSTANT" %}
        {# renders to 'SOME STRING' #}

    {% constant "CONSTANT" as "variable_name" %}
        {# loads the template variable variable_name="SOME STRING" #}
        {# into the template context #}

Design and Security
===================

The ``settings.py`` file often holds many highly sensitive bits of
information, API keys, secrets, passwords, etc...; so exposing the
variables bound in ``settings.py`` directly to the templates would be a
security mistake. However, the ``settings.py`` file still seems like the
proper place to include any constants that should available to
templates.

Because of these facts, we take the whitelist approach which allows you
to maintain security by having to explicitly state what constants are
available to templates, but also have the convenience of being able to
store site wide constants in your ``settings.py`` file.

Contributing
============

Pull, fork, do whatever you'd like with the code.
