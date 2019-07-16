import re
import click
import os
local_slides_url_re = re.compile("\s*\"slides_url\"\s*:\s*\"/?files/(?P<path>.*)\".*")


@click.command()
@click.option("--file", "-f")
def main(file):
    with open(file, "r+", encoding="utf-8") as f:
        for line in f:
            match = local_slides_url_re.match(line)
            if not match:
                continue
            path = match.group("path")
            print(path)
            print(os.path.exists(f"files/{path}"))

if __name__ == "__main__":
    main()

