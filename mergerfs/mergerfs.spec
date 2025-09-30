Name:           mergerfs
Version:        2.41.0~rc1
Release:        1%{?dist}
Summary:        A featureful union filesystem

License:        ISC
URL:            https://github.com/trapexit/mergerfs
Source:         %{url}/archive/%(v=%{version}; echo ${v//\~/-})/%{name}-%(v=%{version}; echo ${v//\~/-}).tar.gz

BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  libatomic

Requires:       fuse

%description
mergerfs is a union filesystem geared towards simplifying storage and
management of files across numerous commodity storage devices. It is
similar to mhddfs, unionfs, and aufs.

%prep
%autosetup -p1 -n %{name}-%(v=%{version}; echo ${v//\~/-})

%build
sed -i 's/$(CHOWN) root/# $(CHOWN) root/' libfuse/Makefile
%make_build

%install
%make_install PREFIX=%{_prefix} DESTDIR=%{buildroot}
mv %{buildroot}%{_prefix}/lib %{buildroot}%{_libdir} || true
mv %{buildroot}/sbin/mount.mergerfs %{buildroot}%{_bindir}
chmod +s %{buildroot}%{_bindir}/mergerfs

%files
%license LICENSE
%doc README.md
%{_bindir}/*.mergerfs
%{_bindir}/mergerfs*
%{_libdir}/mergerfs/preload.so
%{_mandir}/*

%changelog
%autochangelog
