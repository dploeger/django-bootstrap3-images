""" Bootstrap3 image field widget """

from django import forms
from django.conf import settings
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _


class Bootstrap3ImageSelector(forms.TextInput):

    """ A image which can be clicked on and reveals a selector with all
    available bootstrap3-images
    """

    glyphicons = [
        "adjust",
        "align-center",
        "align-justify",
        "align-left",
        "align-right",
        "arrow-down",
        "arrow-left",
        "arrow-right",
        "arrow-up",
        "asterisk",
        "backward",
        "ban-circle",
        "barcode",
        "bell",
        "bold",
        "book",
        "bookmark",
        "briefcase",
        "bullhorn",
        "calendar",
        "camera",
        "certificate",
        "check",
        "chevron-down",
        "chevron-left",
        "chevron-right",
        "chevron-up",
        "circle-arrow-down",
        "circle-arrow-left",
        "circle-arrow-right",
        "circle-arrow-up",
        "cloud",
        "cloud-download",
        "cloud-upload",
        "cog",
        "collapse-down",
        "collapse-up",
        "comment",
        "compressed",
        "copyright-mark",
        "credit-card",
        "cutlery",
        "dashboard",
        "download",
        "download-alt",
        "earphone",
        "edit",
        "eject",
        "envelope",
        "euro",
        "exclamation-sign",
        "expand",
        "export",
        "eye-close",
        "eye-open",
        "facetime-video",
        "fast-backward",
        "fast-forward",
        "file",
        "film",
        "filter",
        "fire",
        "flag",
        "flash",
        "floppy-disk",
        "floppy-open",
        "floppy-remove",
        "floppy-save",
        "floppy-saved",
        "folder-close",
        "folder-open",
        "font",
        "forward",
        "fullscreen",
        "gbp",
        "gift",
        "glass",
        "globe",
        "hand-down",
        "hand-left",
        "hand-right",
        "hand-up",
        "hd-video",
        "hdd",
        "header",
        "headphones",
        "heart",
        "heart-empty",
        "home",
        "import",
        "inbox",
        "indent-left",
        "indent-right",
        "info-sign",
        "italic",
        "leaf",
        "link",
        "list",
        "list-alt",
        "lock",
        "log-in",
        "log-out",
        "magnet",
        "map-marker",
        "minus",
        "minus-sign",
        "move",
        "music",
        "new-window",
        "off",
        "ok",
        "ok-circle",
        "ok-sign",
        "open",
        "paperclip",
        "pause",
        "pencil",
        "phone",
        "phone-alt",
        "picture",
        "plane",
        "play",
        "play-circle",
        "plus",
        "plus-sign",
        "print",
        "pushpin",
        "qrcode",
        "question-sign",
        "random",
        "record",
        "refresh",
        "registration-mark",
        "remove",
        "remove-circle",
        "remove-sign",
        "repeat",
        "resize-full",
        "resize-horizontal",
        "resize-small",
        "resize-vertical",
        "retweet",
        "road",
        "save",
        "saved",
        "screenshot",
        "sd-video",
        "search",
        "send",
        "share",
        "share-alt",
        "shopping-cart",
        "signal",
        "sort",
        "sort-by-alphabet",
        "sort-by-alphabet-alt",
        "sort-by-attributes",
        "sort-by-attributes-alt",
        "sort-by-order",
        "sort-by-order-alt",
        "sound-5-1",
        "sound-6-1",
        "sound-7-1",
        "sound-dolby",
        "sound-stereo",
        "star",
        "star-empty",
        "stats",
        "step-backward",
        "step-forward",
        "stop",
        "subtitles",
        "tag",
        "tags",
        "tasks",
        "text-height",
        "text-width",
        "th",
        "th-large",
        "th-list",
        "thumbs-down",
        "thumbs-up",
        "time",
        "tint",
        "tower",
        "transfer",
        "trash",
        "tree-conifer",
        "tree-deciduous",
        "unchecked",
        "upload",
        "usd",
        "user",
        "volume-down",
        "volume-off",
        "volume-up",
        "warning-sign",
        "wrench",
        "zoom-in",
        "zoom-out",
    ]

    html_image = u"""
    <span id="%(name)s-bootstrapimage" class="glyphicon
    glyphicon-%(image)s"></span>
    """

    html_selector = u"""
    <div class="modal fade" id="imageSelector%(name)s" tabindex="-1"
    role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-body">

                    <ul class="bs-glyphicons">
                    %(images)s
                    </ul>

                </div>
            </div>
        </div>
    </div>
    """

    html_selector_image = u"""

    <li onClick="bootstrap3ImageSelectorSetImage('%(name)s', '%(image)s')">
        <span class="glyphicon glyphicon-%(image)s"></span>
    </li>

    """

    html_widget = u"""
    <p class="form-control-static">
    <div class="well pull-left well-sm glyphicon-well">
    %(image)s&nbsp;
    </div>&nbsp;
    <input type="hidden" id="input-%(name)s" name="%(name)s"
        value="%(current_value)s">
    <button type="button" class="btn btn-default btn-md" data-toggle="modal"
    data-target="#imageSelector%(name)s">
        <span class="glyphicon glyphicon-chevron-down"></span> %(label)s
    </button>
    %(selector)s
    </p>
    """

    class Media:
        css = {
            'all': (settings.STATIC_URL + '/css/colorpicker.css',)
        }
        js = (settings.STATIC_URL + 'colorfield/js/colorpicker.js', )

    def __init__(self, language=None, attrs=None):
        self.language = language or settings.LANGUAGE_CODE[:2]
        super(Bootstrap3ImageSelector, self).__init__(attrs=attrs)

    def render(self, name, value, attrs=None):

        retval = ""

        image_code = '<span id="%(name)s-bootstrapimage"></span>' % {
            'name': name
        }

        # Set image if it exists

        current_value = ""

        if not value is None:

            image_code = mark_safe(
                self.html_image % {
                    'image': value,
                    'name': name
                }
            )

            current_value = value

        # Build up selector

        images = []

        for icon in self.glyphicons:

            images.append(
                mark_safe(
                    self.html_selector_image % {
                        'name': name,
                        'image': icon
                    }
                )
            )

        selector_code = mark_safe(
            self.html_selector % {
                'name': name,
                'images': "\n".join(images)
            }
        )

        # Bring all together for the widget

        retval += mark_safe(self.html_widget % {
            'name': name,
            'image': image_code,
            'selector': selector_code,
            'label': _("Select"),
            'current_value': current_value
        })

        return retval

