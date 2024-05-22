#!/usr/bin/env bash

set -x

sed -i "s|%{?dist}|.patched%{?dist}|g" "$spec"

patch -p1 < ../downstream.patch
cp -r ./* /builddir/build/SOURCES
rpmbuild -bs "$spec"
cp -r /builddir/build/SRPMS/* "$outdir"
