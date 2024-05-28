%define upstreamversion 1.6
%define forkversion 1

Name:       swaylock-effects
Version:    %{upstreamversion}.%{forkversion}
Release:    %autorelease
Summary:    Swaylock, with fancy effects

License:    MIT
URL:	    https://github.com/mortie/swaylock-effects
Source0:    %{url}/archive/v%{upstreamversion}-%{forkversion}/%{name}-v%{upstreamversion}-%{forkversion}.tar.gz

Conflicts:      sway < 1.0

BuildRequires:  gcc
BuildRequires:  meson >= 0.48.0
BuildRequires:  cmake
BuildRequires:  pam-devel
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.14
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  bash-completion
BuildRequires:  fish
BuildRequires:  scdoc

%define program_name swaylock

%description
swaylock-effects is a screen locking utility for Wayland compositors, with fancy effects.

%prep
%autosetup -n %{name}-%{upstreamversion}-%{forkversion}

%build
%meson
%meson_build

%install
%meson_install

%files
%license LICENSE
%doc README.md
%{_bindir}/%{program_name}
%{_mandir}/man1/%{program_name}.1*
%config(noreplace) %{_sysconfdir}/pam.d/%{program_name}

%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/%{program_name}

%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_%{program_name}

%dir %{_datadir}/fish
%dir %{_datadir}/fish/vendor_completions.d
%{_datadir}/fish/vendor_completions.d/%{program_name}.fish

%changelog
%autochangelog
