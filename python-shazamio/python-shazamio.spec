%global pypi_name shazamio

Name:           python-%{pypi_name}
Version:        0.7.0
Release:        %autorelease
Summary:        Reverse engineered Shazam API for Python

License:        MIT
URL:            https://github.com/shazamio/ShazamIO
Source:         %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
Patch:          fix-pyproject.diff

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-audioop-lts

%global _description %{expand:
ShazamIO is a asynchronous framework from reverse engineered Shazam
API written in Python 3.8+ with asyncio and aiohttp.}

%description %{_description}

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %{_description}

%prep
%autosetup -n ShazamIO-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
%pyproject_check_import

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE.txt
%doc README.md

%changelog
%autochangelog
