import subprocess

import tomlkit as toml

from scripts_config import readme_files  # type: ignore

def create_readme():
    with open("README.md", "wt") as r:
        for header, file in readme_files.items():
            r.write(f"\n\n## {header}\n\n")
            with open(file, "rt") as f:
                r.write(f.read())


def update_license():
    with open("LICENSE", "rt") as source, open("docs/license.md", "wt") as target:
        target.write(source.read())


def build_docs():
    print("Building docs...")
    # First, ensure the license is up to date
    update_license()
    # Then, we build the docs
    subprocess.run(["poetry", "run", "mkdocs", "build", "--clean"])
    # Finally, export the readme
    print("Exporting readme...")
    create_readme()
    print("Finished building docs.")


def main():
    build_docs()
    

if __name__ == "__main__":
    main()