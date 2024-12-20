%global pypi_name shazamio-core

Name:           python-%{pypi_name}
Version:        1.0.7
Release:        %autorelease
Summary:        Reverse engineered Shazam API for Python

License:        MIT
URL:            https://github.com/shazamio/shazamio-core
Source:         %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  cargo
BuildRequires:  python3-devel
BuildRequires:  pkgconfig(alsa)

%global _description %{expand:
ShazamIO is a asynchronous framework from reverse engineered Shazam
API written in Python 3.8+ with asyncio and aiohttp.}

%description %{_description}

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %{_description}

%prep
%autosetup -n %{pypi_name}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l shazamio_core

%check
%pyproject_check_import

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
%autochangelog
