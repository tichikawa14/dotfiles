#!/bin/bash

exec docker run --rm -i -e LANG=C.UTF-8 -e LC_ALL=C.UTF-8 -v "$PWD:/mnt:ro" -w /mnt koalaman/shellcheck:latest "$@"
