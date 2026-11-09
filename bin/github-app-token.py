#!/usr/bin/env python3
"""Mint a short-lived GitHub App installation access token.

Reads GH_APP_CLIENT_ID, GH_APP_INSTALLATION_ID, and GH_APP_PRIVATE_KEY_B64 from
the environment, signs a JWT as the App, exchanges it for an installation
access token, and prints only the token to stdout. Intended for use in CI
pipelines mirroring this repo to GitHub over HTTPS (x-access-token:<token>).
"""

import base64
import os
import sys
import time
import urllib.error
import urllib.request
from typing import NoReturn

import json
import jwt

REQUIRED_VARS = ("GH_APP_CLIENT_ID", "GH_APP_INSTALLATION_ID", "GH_APP_PRIVATE_KEY_B64")


def die(message: str) -> NoReturn:
    print(f"github-app-token: {message}", file=sys.stderr)
    sys.exit(1)


def main() -> None:
    missing = [name for name in REQUIRED_VARS if not os.environ.get(name)]
    if missing:
        die(f"missing required environment variable(s): {', '.join(missing)}")

    client_id = os.environ["GH_APP_CLIENT_ID"]
    installation_id = os.environ["GH_APP_INSTALLATION_ID"]

    try:
        private_key = base64.b64decode(os.environ["GH_APP_PRIVATE_KEY_B64"])
    except Exception:
        die("GH_APP_PRIVATE_KEY_B64 is not valid base64")

    now = int(time.time())
    payload = {
        "iat": now - 60,
        "exp": now + 9 * 60,
        "iss": client_id,
    }
    try:
        encoded_jwt = jwt.encode(payload, private_key, algorithm="RS256")
    except Exception as exc:
        die(f"failed to sign JWT: {exc}")

    url = f"https://api.github.com/app/installations/{installation_id}/access_tokens"
    request = urllib.request.Request(
        url,
        method="POST",
        headers={
            "Authorization": f"Bearer {encoded_jwt}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        },
    )

    try:
        with urllib.request.urlopen(request) as response:
            body = json.load(response)
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode(errors="replace")
        die(f"GitHub API returned {exc.code} {exc.reason}: {detail}")
    except Exception as exc:
        die(f"failed to obtain installation access token from GitHub API: {exc}")

    token = body.get("token")
    if not token:
        die("GitHub API response did not include a token")

    print(token)


if __name__ == "__main__":
    main()
