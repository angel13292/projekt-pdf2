from pdf import create_pdf
from jinja2 import Environment, FileSystemLoader
import os

# Capture our current directory
THIS_DIR = os.path.dirname(os.path.abspath(__file__))

def html_doc(variables):
    # Create the jinja2 environment. Notice the use of trim_blocks, which greatly helps control whitespace.
    j2_env = Environment(loader=FileSystemLoader(THIS_DIR), trim_blocks=True)
    return j2_env.get_template('album.html.j2').render(
        variables=variables
    )

def create(albumData):
  pdf = create_pdf(html_doc(albumData))
  return pdf
