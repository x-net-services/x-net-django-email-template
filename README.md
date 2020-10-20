# X-Net Django Email template

This is the default email template that we use in our [company](https://www.x-net.at) for sending emails with django (registration, password forgot, eg.)

## Installation

1. pip install `x_net_django_email_template`
2. Add `x_net_django_email_template` to INSTALLED_APPS

## Usage

When extends the default.html you can overwrite the blocks:

```html
{% extends "email/default.html" %}

{% load html_email i18n %}

{% block title %}Title{% endblock %}
{% block header_title %}Header title{% endblock %}

{% block main %}
  <p>This is an example of text.</p>

  <table role="presentation">
      <tr>
      <td class="button-wrapper">
        <table class="button" role="presentation">
          <tr>
            <td>
              <a href="#">Click me</a>
            </td>
          </tr>
        </table>
      </td>
    </tr>
  </table>
{% endblock %}

{% block footer %}
  <p><small>{% trans "This is an automatically generated email, please do not reply to this message." %}</small></p>
{% endblock %}
````

### Templatetags

With the `full_static` template tag you can insert absolute urls in the email template.

```html
{% load html_email %}
<link rel="stylesheet" href="{% full_static "css/email/html-email.min.css" %}" />
```
