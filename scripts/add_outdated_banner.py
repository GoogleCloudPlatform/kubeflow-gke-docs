"""Copyright 2018-2022 The Kubeflow Authors

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    https://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

Mark outdated docs as requiring updating

This script finds all markdown files under `content/` that haven't been updated
recently (default 30 days) according to git, and adds a header warning that the
file is out of date.

Example usage:

    python scripts/add_outdated_banner.py --old-version 1.0 --new-version 1.1
"""

import argparse
import re
from datetime import datetime, timedelta
from pathlib import Path
from subprocess import check_output


WARNING = """

{{%% alert title="Out of date" color="warning" %%}}
This guide contains outdated information pertaining to Kubeflow %s. This guide
needs to be updated for Kubeflow %s.
{{%% /alert %%}}

"""

WARNING_REGEX = r"""

{{% alert title="Out of date".*{{% /alert %}}

"""


def main(warning_text: str, cutoff: timedelta):
    now = datetime.utcnow().astimezone()

    for md in Path("content/").rglob("*.md"):
        last_changed = check_output(
            ["git", "log", "-1", "--pretty=format:%ci", md]
        ).decode("utf-8")
        last_changed = datetime.strptime(last_changed, "%Y-%m-%d %H:%M:%S %z")

        # If the docs are recent, don't add the header
        if now - last_changed < cutoff:
            continue

        contents = md.read_text()

        # If the doc already has an out of date warning, replace it with the new one
        if re.search(WARNING_REGEX, contents, flags=re.MULTILINE | re.DOTALL):
            md.write_text(
                re.sub(
                    WARNING_REGEX,
                    warning_text,
                    contents,
                    flags=re.MULTILINE | re.DOTALL,
                )
            )
        # Otherwise, check to see if there's a front matter section delimited by `+++`. If so,
        # add the out of date warning directly afterwards.
        else:
            pluses = list(re.finditer(r"\+\+\+", contents))
            if len(pluses) == 2:
                p = pluses[1]

                # If there's only a front matter section and no actual content, don't bother
                # adding the warning.
                if contents[p.end():].strip():
                    md.write_text(contents[:p.end()] + warning_text + contents[p.end():])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Mark old docs as requiring updating")

    parser.add_argument(
        "--old-version",
        required=True,
        help="The docs version that is considered out of date",
    )
    parser.add_argument("--new-version", required=True, help="The newest docs version")
    parser.add_argument(
        "--cutoff",
        default=30,
        type=int,
        help="Cutoff in days that a document must have been "
        "updated within to not be considered out of date",
    )
    args = parser.parse_args()

    main(WARNING % (args.old_version, args.new_version), timedelta(days=args.cutoff))