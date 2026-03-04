Name:           cpptrace
Version:        1.0.4
Release:        %autorelease
Summary:        Cpptrace is a simple and portable C++ stacktrace library 

License:        MIT
URL:            https://github.com/jeremy-rifkin/cpptrace
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libcxxabi-devel
BuildRequires:  pkgconfig(libdwarf)
BuildRequires:  pkgconfig(libunwind)
BuildRequires:  pkgconfig(libzstd)

%description
Cpptrace is a simple and portable C++ stacktrace library supporting
C++11 and greater on Linux, macOS, and Windows including MinGW and
Cygwin environments. The goal: Make stack traces simple for once.

In addition to providing access to stack traces, cpptrace also
provides a mechanism for getting stacktraces from thrown exceptions
which is immensely valuable for debugging and triaging.

%package devel
Summary: Development files for cpptrace

%description devel
Development files for cpptrace

%prep
%autosetup -C -p1

%build
%cmake \
    -DCPPTRACE_DEMANGLE_WITH_CXXABI=ON \
    -DCPPTRACE_FIND_LIBDWARF_WITH_PKGCONFIG=ON \
    -DCPPTRACE_USE_EXTERNAL_ZSTD=ON \
    -DCPPTRACE_USE_EXTERNAL_LIBDWARF=ON \
    -DCPPTRACE_UNWIND_WITH_LIBUNWIND=ON \
    -DBUILD_TESTING=OFF \
    -DBUILD_SHARED_LIBS=ON
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%{_libdir}/libcpptrace.so.*

%files devel
%license LICENSE
%{_libdir}/libcpptrace.so
%{_libdir}/libcpptrace.so.*
%{_libdir}/cmake/cpptrace
%{_includedir}/ctrace
%{_includedir}/cpptrace

%changelog
%autochangelog
