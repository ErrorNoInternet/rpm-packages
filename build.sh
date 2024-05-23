#!/usr/bin/env bash

set -x

sed -i "s|%{?dist}|.patched%{?dist}|" "$spec"
sed -i "s|%autorelease|%autorelease -e patched|" "$spec"
sed -i "s|-S git_am|-S git|" "$spec"
patch -p1 < ../downstream.patch

cp -r ./* /builddir/build/SOURCES
rpmbuild -bs "$spec"
cp -r /builddir/build/SRPMS/* "$outdir"
