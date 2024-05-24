#!/usr/bin/env bash

set -x

dnf install -y git fedpkg
git config --global --add safe.directory "$(pwd)"

git checkout f40
sed -i "s|\([^%]\)%{?dist}|\1.patched%{?dist}|" "$spec"
sed -i "s|%autorelease|%autorelease -e patched|" "$spec"
sed -i "s|-S git_am|-S git|" "$spec"

patch -p1 < ../downstream.patch

fedpkg srpm
cp -r ./*.src.rpm "$outdir"
