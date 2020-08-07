"""
Add a frame around LaTeX code-block directive
"""
from sphinx.writers.latex import LaTeXTranslator

class MyLaTeXTranslator(LaTeXTranslator):
    def visit_literal_block(self, node):
        return ''.join([
            'foo',
            super().visit_literal_block(node),
            'bar'
        ])

def setup(app):
    app.set_translator('latex', MyLaTeXTranslator)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
