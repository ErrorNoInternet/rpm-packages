%global pypi_name pydub

Name:           python-%{pypi_name}
Version:        0.25.1
Release:        %autorelease
Summary:        Manipulate audio with a high level interface

License:        MIT
URL:            https://github.com/jiaaro/pydub
Source:         %{url}/archive/v%{version}/%{pypi_name}-v%{version}.tar.gz

BuildRequires:  cargo
BuildRequires:  python3-devel
BuildRequires:  python3-audioop-lts

%global _description %{expand:
Manipulate audio with an simple and easy high level interface.}

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
%pyproject_save_files -l %{pypi_name}

%check
%pyproject_check_import

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
%autochangelog
