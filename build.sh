#!/usr/bin/env bash

set -x

dnf install -y fedpkg

sed -i "s|%{?dist}|.patched%{?dist}|" "$spec"
sed -i "s|%autorelease|%autorelease -e patched|" "$spec"
sed -i "s|-S git_am|-S git|" "$spec"

patch -p1 < ../downstream.patch

cp -r ./* /builddir/build/SOURCES
fedpkg srpm
cp -r ./*.src.rpm "$outdir"
