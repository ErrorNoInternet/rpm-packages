%global lss_version 2024.02.01

Name:               breakpad
Version:            2024.02.16
Release:            %autorelease
Summary:            Google Breakpad crash-reporting system

License:            BSD-3-Clause
URL:                https://chromium.googlesource.com/breakpad/breakpad
Source0:            %{url}/+archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:            https://chromium.googlesource.com/linux-syscall-support/+archive/v%{lss_version}.tar.gz#/linux-syscall-support-%{lss_version}.tar.gz

BuildRequires:      gcc-c++
BuildRequires:      pkgconfig(gmock)
BuildRequires:      pkgconfig(gtest)
BuildRequires:      pkgconfig(zlib)

%description
A set of client and server components which implement a crash-reporting system.

%package devel
Summary: Development files for %{name}
Requires: %{name}-static%{?_isa} = %{version}-%{release}

%description devel
Development files for the Google Breakpad crash-reporting system.

%package static
Summary: Static library for %{name}

%description static
Static library for the Google Breakpad crash-reporting system.

%prep
%autosetup -C
mkdir -p src/third_party/lss
tar xf %{SOURCE1} -C src/third_party/lss

%conf
export CXXFLAGS="%{build_cxxflags} -Wno-error=array-bounds -Wno-maybe-uninitialized"
%configure

%build
%make_build

%install
%make_install
rm -rf %{buildroot}%{_docdir}/breakpad-0.1

%files
%license LICENSE
%doc AUTHORS
%doc ChangeLog
%doc INSTALL
%doc NEWS
%doc README.md
%{_bindir}/core2md
%{_bindir}/dump_syms
%ifarch %{x86_64} %{ix86}
%{_bindir}/dump_syms_mac
%endif
%{_bindir}/microdump_stackwalk
%{_bindir}/minidump-2-core
%{_bindir}/minidump_dump
%{_bindir}/minidump_stackwalk
%{_bindir}/minidump_upload
%{_bindir}/pid2md
%{_bindir}/sym_upload
%{_libexecdir}/core_handler

%files -n %{name}-devel
%license LICENSE
%{_includedir}/breakpad
%{_libdir}/pkgconfig/breakpad-client.pc
%{_libdir}/pkgconfig/breakpad.pc

%files -n %{name}-static
%license LICENSE
%{_libdir}/libbreakpad.a
%{_libdir}/libbreakpad_client.a

%changelog
%autochangelog
