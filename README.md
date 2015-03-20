django-tagconstants
===================

Define constants in your settings file, that are then made available in your templates.

# Installation

From the command line:

```
pip install django-tagconstants
```

Add tagconstants to your installed apps:

```python
INSTALLED_APPS = (
	...
	'tagconstants',
	...
)
```

Create a `TAG_CONSTANTS` dictionary in your `settings.py` file:

```python
TAG_CONSTANTS = {}
```

# Usage

For security purposes, `tagconstants` is designed so that you create a whitelist  of variables to make available in your templates. For more information see the **Design and Security** section.

To use a constant in your templates, first add the constant to your `TAG_CONSTANTS` setting:

```python
TAG_CONSTANTS = {
	'CONSTANT': 'SOME STRING',
}
```

Then in your templates, you can recall these constants with the `{% constant ... %}` template tag:

```html
{% load tagconstants %}

{% constant "CONSTANT" %}
    {# renders to 'SOME STRING' #}

{% constant "CONSTANT" as "variable_name" %}
	{# loads the template variable variable_name="SOME STRING" #}
	{# into the template context #}
```

# Contributing

Pull, fork, do whatever you'd like with the code.

