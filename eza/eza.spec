%bcond check 1

%global cargo_install_lib 0

Name:           eza
Version:        0.23.2
Release:        %autorelease
Summary:        A modern alternative to ls 

# 0BSD OR MIT OR Apache-2.0
# Apache-2.0 OR BSL-1.0
# Apache-2.0 OR MIT
# Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
# EUPL-1.2
# MIT
# MIT OR Apache-2.0
# MIT OR Apache-2.0 OR CC0-1.0
# MIT OR Zlib OR Apache-2.0
# MPL-2.0
# Unicode-3.0
# Unlicense OR MIT
License:        (0BSD OR MIT OR Apache-2.0) AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND EUPL-1.2 AND MIT AND (MIT OR Apache-2.0) AND (MIT OR Apache-2.0 OR CC0-1.0) AND (MIT OR Zlib OR Apache-2.0) AND MPL-2.0 AND Unicode-3.0 AND (Unlicense OR MIT)
SourceLicense:  EUPL-1.2

URL:            https://github.com/eza-community/eza
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch:          directory-size-optimization.diff

BuildRequires:  cargo-rpm-macros >= 26
BuildRequires:  pandoc

%global _description %{expand:
eza is a modern alternative for the venerable file-listing command-line program
`ls` that ships with Unix and Linux operating systems, giving it more features
and better defaults. It uses colours to distinguish file types and metadata. It
knows about symlinks, extended attributes, and Git. And it’s small, fast, and
just one single binary.}

%description %{_description}

%package bash-completion
BuildArch:      noarch
Summary:        Bash completion files for %{name}
Provides:       %{name}-bash-completion = %{version}-%{release}

Requires:       bash-completion
Requires:       %{name} = %{version}-%{release}

%description bash-completion
This package installs Bash completion files for %{name}

%package fish-completion
BuildArch:      noarch
Summary:        Fish completion files for %{name}
Provides:       %{name}-fish-completion = %{version}-%{release}

Requires:       fish
Requires:       %{name} = %{version}-%{release}

%description fish-completion
This package installs Fish completion files for %{name}

%package zsh-completion
BuildArch:      noarch
Summary:        Zsh completion files for %{name}
Provides:       %{name}-zsh-completion = %{version}-%{release}

Requires:       zsh
Requires:       %{name} = %{version}-%{release}

%description zsh-completion
This package installs Zsh completion files for %{name}

%prep
%autosetup -p1
cargo vendor
%cargo_prep -v vendor

%build
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%{cargo_vendor_manifest}

%install
%cargo_install

for manpage in eza.1 eza_colors.5 eza_colors-explanation.5; do
    sed "s/\$version/v${version}/g" "man/${manpage}.md" |
        pandoc --standalone -f markdown -t man > "man/${manpage}"
done
install -Dpm644 man/*.1 -t %{buildroot}%{_mandir}/man1/
install -Dpm644 man/*.5 -t %{buildroot}%{_mandir}/man5/

install -Dpm644 completions/bash/%{name} -t %{buildroot}/%{bash_completions_dir}/
install -Dpm644 completions/fish/%{name}.fish -t %{buildroot}/%{fish_completions_dir}/
install -Dpm644 completions/zsh/_%{name} -t %{buildroot}/%{zsh_completions_dir}/

%if %{with check}
%check
%cargo_test
%endif

%files
%license cargo-vendor.txt
%license LICENSE.dependencies
%license LICENSE.txt
%license LICENSES/*
%doc CHANGELOG.md
%doc CODE_OF_CONDUCT.md
%doc CONTRIBUTING.md
%doc INSTALL.md
%doc README.md
%doc SECURITY.md
%doc TESTING.md
%{_bindir}/eza
%{_mandir}/man1/*
%{_mandir}/man5/*

%files bash-completion
%{bash_completions_dir}/%{name}

%files fish-completion
%{fish_completions_dir}/%{name}.fish

%files zsh-completion
%{zsh_completions_dir}/_%{name}

%changelog
%autochangelog
