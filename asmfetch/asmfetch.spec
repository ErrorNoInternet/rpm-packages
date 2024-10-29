%global commit      656b1611b2f2c8b70db191977b82c8cb057ca238
%global snapdate    20240920

Name:               asmfetch
Version:            0^%{snapdate}g%(c=%{commit}; echo ${c:0:7})
Release:            %autorelease
Summary:            A fetch tool written in x86-64 assembly for Linux

License:            LGPL-3.0-or-later
URL:                https://github.com/ErrorNoInternet/asmfetch
Source:             %{url}/archive/%{commit}/%{name}-%{commit}.tar.gz

BuildRequires:      gcc

%description
A fetch tool written in x86-64 assembly for Linux.
Runs in under 150 microseconds and has zero dependencies.

%prep
%autosetup -n %{name}-%{commit} -p1

%build
gcc -nostdlib %{optflags} asmfetch.S -o asmfetch

%install
mkdir -p %{buildroot}%{_bindir}
mv asmfetch %{buildroot}%{_bindir}

%files
%license LICENSE
%doc README.md
%{_bindir}/asmfetch

%changelog
%autochangelog