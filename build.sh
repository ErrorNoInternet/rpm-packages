#!/usr/bin/env bash

set -x

dnf install -y git fedpkg

non_patched=(
    "quickshell/quickshell-git.spec"
)

should_patch=true
for file in "${non_patched[@]}"; do
    if [[ $spec == *$file ]]; then
        should_patch=false
        break
    fi
done

if $should_patch; then
    git config --global --add safe.directory "$PWD"
    git checkout f42

    patch -p1 <../downstream.diff || {
        echo "downstream diff failed to apply"
        exit 1
    }
    printf "%s\n%s\n" "%global _default_patch_fuzz 2" "$(cat "$spec")" >"$spec"
    sed -i "s|\([^%]\)%{?dist}|\1.patched%{?dist}|" "$spec"
    sed -i "s|%autorelease|%autorelease -e patched|" "$spec"
    sed -i "s|-S git_am|-S git|" "$spec"

    fedpkg srpm
else
    NO_GIT=1 ../update.sh "$spec"
    rpmbuild -bs "$spec" \
        --define "_topdir ." \
        --define "_sourcedir ." \
        --define "_srcrpmdir ."
fi

cp ./*.src.rpm "$outdir"
