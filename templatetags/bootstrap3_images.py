""" Template tags for Bootstrap3 Imageselector """

from django import template

register = template.Library()


@register.simple_tag()
def bootstrap3_imageselector_head():
    """ Needed Head tags for the imageselector
    """

    return """

    <style type="text/css">
    /*
     * Glyphicons
     *
     * Special styles for displaying the icons and their classes in the docs.
     * (Adapted from official Bootstrap documentation site)
     */

    .bs-glyphicons {
      padding-left: 0;
      padding-bottom: 1px;
      margin-bottom: 20px;
      list-style: none;
      overflow: hidden;
    }
    .bs-glyphicons li {
      float: left;
      width: 25%;
      padding: 10px;
      margin: 0 -1px -1px 0;
      font-size: 8px;
      line-height: 1.4;
      text-align: center;
      border: 1px solid #ddd;
    }
    .bs-glyphicons .glyphicon {
      margin-top: 5px;
      margin-bottom: 10px;
      font-size: 14px;
    }
    .bs-glyphicons .glyphicon-class {
      display: block;
      text-align: center;
    }
    .bs-glyphicons li:hover {
      background-color: rgba(86,61,124,.1);
    }

    @media (min-width: 768px) {
      .bs-glyphicons li {
        width: 7%;
      }
    }

    .glyphicon-well {

      padding: 6px;

    }
    </style>

    <script type="text/javascript">
    function bootstrap3ImageSelectorSetImage(inputName, imageName) {

        // Set to hidden input

        $("#input-" + inputName).val(imageName);

        // Update display image

        $("#" + inputName + "-bootstrapimage").removeClass()
            .addClass("glyphicon")
            .addClass("glyphicon-" + imageName);

        // Popdown selector

        $("#imageSelector" + inputName).modal('hide');

    }
    </script>

    """

