#!/bin/sh

XDG_CONFIG_HOME=${XDG_CONFIG_HOME:-~/.config}
if [ -f "$XDG_CONFIG_HOME"/vesktop-flags.conf ]; then
    VESKTOP_USER_FLAGS="$(grep -v '^#' "$XDG_CONFIG_HOME"/vesktop-flags.conf)"
fi

VESKTOP_BIN=/usr/lib/vesktop/vesktop
if [ -f "/usr/lib64/vesktop/vesktop" ]; then
    VESKTOP_BIN=/usr/lib64/vesktop/vesktop
fi

# shellcheck disable=SC2086
exec $VESKTOP_BIN $VESKTOP_USER_FLAGS "$@"
