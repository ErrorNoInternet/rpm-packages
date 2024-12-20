%global pypi_name audioop-lts

Name:           python-%{pypi_name}
Version:        0.2.1
Release:        %autorelease
Summary:        LTS Port of Python audioop

License:        MIT
URL:            https://github.com/AbstractUmbra/audioop
Source:         %{url}/archive/%{version}/audioop-%{version}.tar.gz

BuildRequires:  cargo
BuildRequires:  python3-devel

%global _description %{expand:
An LTS port of the Python builtin module audioop which was deprecated
since version 3.11 and removed in 3.13.}

%description %{_description}

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %{_description}

%prep
%autosetup -n audioop-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l audioop

%check
%pyproject_check_import

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
%autochangelog
