Name:           shaq
Version:        0.0.5
Release:        %autorelease
Summary:        A CLI client for Shazam

License:        MIT
URL:            https://github.com/woodruffw/shaq
Source:         %{url}/archive/v%{version}/%{name}-v%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

%description
A bare-bones CLI client for Shazam.

%prep
%autosetup -p1

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install

%files
%license LICENSE
%doc README.md
%{_bindir}/shaq

%changelog
%autochangelog
