#!/usr/bin/env bash

set -x

dnf install -y git fedpkg
git config --global --add safe.directory "$PWD"
git checkout f40

patch -p1 < ../downstream.diff
printf "%s\n%s\n" "%global _default_patch_fuzz 2" "$(cat "$spec")" > "$spec"
sed -i "s|\([^%]\)%{?dist}|\1.patched%{?dist}|" "$spec"
sed -i "s|%autorelease|%autorelease -e patched|" "$spec"
sed -i "s|-S git_am|-S git|" "$spec"

fedpkg srpm
cp ./*.src.rpm "$outdir"
