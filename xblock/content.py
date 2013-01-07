"""Content-oriented XBlocks."""

from string import Template

from .core import XBlock, String, Scope
from .fragment import Fragment


class HelloWorldBlock(XBlock):
    """A simple block: just show some fixed content."""
    @XBlock.view('default')
    def student_view(self, context):
        return Fragment(u"Hello, world!")


class HtmlBlock(XBlock):
    """Render content as HTML.

    The content can have $PLACEHOLDERS, which will be substituted with values
    from the context.

    """

    content = String(help="The HTML to display", scope=Scope.content, default=u"<b>DEFAULT</b>")

    @XBlock.view('default')
    def student_view(self, context):
        return Fragment(Template(self.content).substitute(**context))
