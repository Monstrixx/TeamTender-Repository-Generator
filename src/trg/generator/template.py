"""
Template Generator
"""

from pathlib import Path


class TemplateGenerator:

    def create_readme(self, project_name: str, output_dir: str):

        readme = Path(output_dir) / "README.md"

        content = f"""# {project_name}

Generated automatically by TRG.

"""

        readme.write_text(content, encoding="utf-8")