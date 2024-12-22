%global commit      1f172d2a63f341f99120c32d0aa2c902cdee60b6
%global snapdate    20220822

Name:           shazamctl
Version:        0^%{snapdate}g%(c=%{commit}; echo ${c:0:7})
Release:        %autorelease
Summary:        A toy command-line client for Shazam

License:        MIT
URL:            https://github.com/notpushkin/shazamctl
Source:         %{url}/archive/%{commit}/%{name}-%{commit}.tar.gz
Patch:          fix-pyproject.diff

BuildArch:      noarch
BuildRequires:  python3-devel

%description
A toy command-line client for Shazam.

%prep
%autosetup -n %{name}-%{commit} -p1

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files shazamctl

%files -f %{pyproject_files}
%license LICENSE
%doc README.md
%{_bindir}/shazamctl

%changelog
%autochangelog
