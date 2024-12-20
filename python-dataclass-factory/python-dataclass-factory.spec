%global pypi_name dataclass-factory

Name:           python-%{pypi_name}
Version:        2.16
Release:        %autorelease
Summary:        An utility class for creating instances of dataclasses

License:        MIT
URL:            https://github.com/reagento/adaptix
Source:         %{url}/archive/%{version}/adaptix-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
dataclass_factory is a modern way to convert dataclasses or other
objects to and from more common types like dicts}

%description %{_description}

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %{_description}

%prep
%autosetup -n adaptix-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l dataclass_factory

%check
%pyproject_check_import

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
%autochangelog
