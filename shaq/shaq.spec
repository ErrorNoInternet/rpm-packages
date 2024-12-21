Name:           shaq
Version:        0.0.5
Release:        %autorelease
Summary:        A CLI client for Shazam

License:        MIT
URL:            https://github.com/woodruffw/shaq
Source:         %{url}/archive/v%{version}/%{name}-v%{version}.tar.gz
Patch0:         fix-pyproject.diff
Patch1:         improvements.diff

BuildArch:      noarch
BuildRequires:  python3-devel
Requires:       python-audioop-lts

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
%pyproject_save_files shaq

%files -f %{pyproject_files}
%license LICENSE
%doc README.md
%{_bindir}/shaq

%changelog
%autochangelog
