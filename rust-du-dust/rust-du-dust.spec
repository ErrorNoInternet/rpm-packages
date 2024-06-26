# Generated by rust2rpm 26
%bcond_without check

%global crate du-dust

Name:           rust-du-dust
Version:        1.0.0
Release:        2%{?dist}
Summary:        More intuitive version of du

License:        Apache-2.0
URL:            https://crates.io/crates/du-dust
Source:         %{crates_source}
# Automatically generated patch to strip dependencies and normalize metadata
Patch:          du-dust-fix-metadata-auto.diff

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
A more intuitive version of du.}

%description %{_description}

%package     -n %{crate}
Summary:        %{summary}
# FIXME: paste output of %%cargo_license_summary here
License:        # FIXME
# LICENSE.dependencies contains a full license breakdown

%description -n %{crate} %{_description}

%package bash-completion
BuildArch:      noarch
Summary:        Bash completion files for %{crate}
Provides:       %{crate}-bash-completion = %{version}-%{release}

Requires:       bash-completion
Requires:       %{crate} = %{version}-%{release}

%description bash-completion
This package installs Bash completion files for %{crate}

%package fish-completion
BuildArch:      noarch
Summary:        Fish completion files for %{crate}
Provides:       %{crate}-fish-completion = %{version}-%{release}

Requires:       fish
Requires:       %{crate} = %{version}-%{release}

%description fish-completion
This package installs Fish completion files for %{crate}

%package zsh-completion
BuildArch:      noarch
Summary:        Zsh completion files for %{crate}
Provides:       %{crate}-zsh-completion = %{version}-%{release}

Requires:       zsh
Requires:       %{crate} = %{version}-%{release}

%description zsh-completion
This package installs Zsh completion files for %{crate}

%files       -n %{crate}
%license LICENSE
%license LICENSE.dependencies
%license cargo-vendor.txt
%doc README.md
%{_bindir}/dust
%{_mandir}/man1/dust.1*

%files bash-completion
%{bash_completions_dir}/dust

%files zsh-completion
%{zsh_completions_dir}/_dust

%files fish-completion
%{fish_completions_dir}/dust.fish

%prep
%autosetup -n %{crate}-%{version} -p1
cargo vendor
%cargo_prep -v vendor

%build
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%{cargo_vendor_manifest}

%install
%cargo_install

install -Dpm644 man-page/dust.1 %{buildroot}%{_mandir}/man1/dust.1

install -Dpm644 completions/dust.bash %{buildroot}%{bash_completions_dir}/dust
install -Dpm644 completions/dust.fish %{buildroot}%{fish_completions_dir}/dust.fish
install -Dpm644 completions/_dust %{buildroot}%{zsh_completions_dir}/_dust

%if %{with check}
%check
%cargo_test
%endif

%changelog
%autochangelog
