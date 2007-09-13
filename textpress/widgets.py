# -*- coding: utf-8 -*-
"""
    textpress.widgets
    ~~~~~~~~~~~~~~~~~

    This module provides the core widgets and functionality to build your
    own.  Widgets are, in the context of TextPress, classes that have a
    unicode conversion function that renders a template into a string but
    have all their attributes attached to themselves.  This gives template
    designers the ability to change the general widget template but also
    render one widget differently.

    Additionally widgets could be moved around from the admin panel in the
    future.

    :copyright: Copyright 2007 by Armin Ronacher
    :license: GNU GPL.
"""
from textpress.application import render_template
from textpress import models


class Widget(object):
    """
    Baseclass for all the widgets out there!
    """

    #: name of the template for this widget. Please prefix those template
    #: names with an underscore to mark it as partial. The widget is available
    #: in the template as `widget`.
    TEMPLATE = None

    def get_widget_metadata(self):
        """This function should return some metadata for the admin panel."""

    def __unicode__(self):
        return render_template(self.TEMPLATE, widget=self)


class TagCloud(Widget):
    """
    A tag cloud. What else?
    """

    TEMPLATE = '_tagcloud.html'

    def __init__(self, max=None):
        self.tags = models.get_tag_cloud(max)


class PostArchiveSummary(Widget):
    """
    Show the last n months/years/days with posts.
    """

    TEMPLATE = '_post_archive_summary.html'

    def __init__(self, detail='months', limit=6):
        self.__dict__.update(models.get_post_archive_summary(detail, limit))


all_widgets = {
    'get_tag_cloud':                TagCloud,
    'get_post_archive_summary':     PostArchiveSummary
}