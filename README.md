# Boostrap3-Images

Django model field and widget for storing, retrieving and displaying
bootstrap3 glyphicon-images

## Introduction

bootstrap3_images is a django model field and widget for storing and
retrieving images from the Bootstrap3 glyphicon list. It supports selecting
those images using a image selector widget.

It obviously uses the Bootstrap3 glyphicons, so
[Glyphicons](http://glyphicons.com/) should be praised here.

## Requirements

You need an integration of Bootstrap3 in your Django app. I recommend using
[Django-Bootstrap3](https://github.com/dyve/django-bootstrap3) for that.

## Installation

Install the app using pypi or the manual way by downloading the archive and
expanding it into your django project and add it to the INSTALLED_APPS-setting:

    INSTALLED_APPS=(

       # ...

       "bootstrap3_images",

       # ...

    )

## Usage

To use the django field, import the module:

    from bootstrap3_images.fields import Bootstrap3ImageField

and use "Bootstrap3ImageField" like a "CharField" model field (you don't have
 to specify max_length, though):

    image = Bootstrap3ImageField(
        name="MyImage"
    )

If you want to use the selector in a template, be sure to load the
template tags for it:

    {% load bootstrap3_images %}

and call this template tag inside your <head>-Definition:

    {% bootstrap3_imageselector_head %}
