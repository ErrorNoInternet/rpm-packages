# Generated by rust2rpm 27
%bcond check 1

%global short_name jj

Name:           jujutsu
Version:        0.26.0
Release:        %autorelease
Summary:        An experimental version control system

# (Apache-2.0 OR MIT) AND BSD-3-Clause
# (MIT OR Apache-2.0) AND Unicode-DFS-2016
# 0BSD OR MIT OR Apache-2.0
# Apache-2.0
# Apache-2.0 OR BSL-1.0
# Apache-2.0 OR BSL-1.0 OR MIT
# Apache-2.0 OR MIT
# Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
# BSD-2-Clause OR Apache-2.0 OR MIT
# BSD-3-Clause
# CC0-1.0 OR MIT-0 OR Apache-2.0
# MIT
# MIT OR Apache-2.0
# MIT OR Apache-2.0 OR Zlib
# MIT OR Zlib OR Apache-2.0
# MPL-2.0
# Unicode-3.0
# Unlicense OR MIT
# Zlib OR Apache-2.0 OR MIT
License:        ((Apache-2.0 OR MIT) AND BSD-3-Clause) AND ((MIT OR Apache-2.0) AND Unicode-DFS-2016) AND (0BSD OR MIT OR Apache-2.0) AND Apache-2.0 AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR BSL-1.0 OR MIT) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND BSD-3-Clause AND (CC0-1.0 OR MIT-0 OR Apache-2.0) AND MIT AND (MIT OR Apache-2.0) AND (MIT OR Apache-2.0 OR Zlib) AND (MIT OR Zlib OR Apache-2.0) AND MPL-2.0 AND Unicode-3.0 AND (Unlicense OR MIT) AND (Zlib OR Apache-2.0 OR MIT)
SourceLicense:  Apache-2.0

URL:            https://github.com/jj-vcs/jj
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

Provides:       %{short_name} = %{version}-%{release}

BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  openssh
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(zlib)

Recommends:     git

%global _description %{expand:
Jujutsu is a powerful version control system for software projects. You use it
to get a copy of your code, track changes to the code, and finally publish those
changes for others to see and use. It is designed from the ground up to be easy
to use - whether you are new or experienced, working on brand new projects
alone, or large scale software projects with large histories and teams.}

%description %{_description}

%package doc
BuildArch:      noarch
Summary:        Documentation files for %{name}
Requires:       %{name} = %{version}-%{release}

%description doc
This package installs additional documentation files for %{name}

%package bash-completion
BuildArch:      noarch
Summary:        Bash completion files for %{name}

Requires:       bash-completion
Requires:       %{name} = %{version}-%{release}

%description bash-completion
This package installs Bash completion files for %{name}

%package fish-completion
BuildArch:      noarch
Summary:        Fish completion files for %{name}

Requires:       fish
Requires:       %{name} = %{version}-%{release}

%description fish-completion
This package installs Fish completion files for %{name}

%package zsh-completion
BuildArch:      noarch
Summary:        Zsh completion files for %{name}

Requires:       zsh
Requires:       %{name} = %{version}-%{release}

%description zsh-completion
This package installs Zsh completion files for %{name}

%prep
%autosetup -n %{short_name}-%{version} -p1
cargo vendor
%cargo_prep -v vendor

%build
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%{cargo_vendor_manifest}

%install
pushd cli
%cargo_install
popd

mkdir -p %{buildroot}%{bash_completions_dir}
mkdir -p %{buildroot}%{fish_completions_dir}
mkdir -p %{buildroot}%{zsh_completions_dir}
mkdir -p %{buildroot}%{_mandir}

exe=target/release/%{short_name}
$exe util completion bash > %{buildroot}%{bash_completions_dir}/%{short_name}
$exe util completion fish > %{buildroot}%{fish_completions_dir}/%{short_name}.fish
$exe util completion zsh > %{buildroot}%{zsh_completions_dir}/_%{short_name}
$exe util install-man-pages %{buildroot}%{_mandir}

cp -a --remove-destination cli/src/config-schema.json docs/

%if %{with check}
%check
%cargo_test
%endif

%files
%license LICENSE
%license LICENSE.dependencies
%license cargo-vendor.txt
%doc AUTHORS
%doc CHANGELOG.md
%doc README.md
%doc SECURITY.md
%{_bindir}/%{short_name}
%{_mandir}/man*

%files doc
%doc docs/*

%files bash-completion
%{bash_completions_dir}/%{short_name}

%files fish-completion
%{fish_completions_dir}/%{short_name}.fish

%files zsh-completion
%{zsh_completions_dir}/_%{short_name}

%changelog
%autochangelog
