%define _fortify_level 2

Name:           scrcpy
Version:        3.3.4
Release:        %autorelease
Summary:        Display and control your Android device
License:        Apache-2.0

URL:            https://github.com/Genymobile/scrcpy
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{url}/releases/download/v%{version}/%{name}-server-v%{version}

BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  java-devel >= 11
BuildRequires:  meson

BuildRequires:  pkgconfig(ffms2)
BuildRequires:  pkgconfig(libavdevice)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  vulkan-loader

Requires:       android-tools

# https://github.com/Genymobile/scrcpy/blob/master/FAQ.md#issue-with-wayland
Recommends:     libdecor

%description
This application provides display and control of Android devices
connected on USB (or over TCP/IP).

%package bash-completion
BuildArch:      noarch
Summary:        Bash completion files for %{name}
Provides:       %{name}-bash-completion = %{version}-%{release}

Requires:       bash-completion
Requires:       %{name} = %{version}-%{release}

%description bash-completion
This package installs Bash completion files for %{name}

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

%build
%meson -Db_lto=true -Dprebuilt_server='%{SOURCE1}'
%meson_build

%install
%meson_install

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}{,-console}.desktop

%files
%license LICENSE
%doc README.md FAQ.md
%{_bindir}/%{name}
%{_datadir}/%{name}/%{name}-server
%{_mandir}/man1/%{name}.1*
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/applications/*.desktop

%files bash-completion
%{bash_completions_dir}/%{name}

%files zsh-completion
%{zsh_completions_dir}/_%{name}

%changelog
%autochangelog
