
from importlib.machinery import SourceFileLoader
import os
from render import tex
from resume_types import make_resume_model
import subprocess
import sys


def make(output_format, resume_file, output_dir):
    my_resume = SourceFileLoader('my_resume', resume_file).load_module()
    resume_model = make_resume_model(my_resume)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    if output_format == 'tex':
        with open(os.path.join(output_dir, 'resume.tex'), 'w') as f:
            resume_str = tex.render(resume_model)
            f.write(resume_str)

        subprocess.call(['bash', 'scripts/make_pdf.sh', output_dir])


if __name__ == '__main__':
    output_format, resume_file, output_dir = sys.argv[1:4]
    make(output_format, resume_file, output_dir)
