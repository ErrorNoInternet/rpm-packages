Name:           swaylock-effects
Version:        1.7.0.0
Release:        %autorelease
Summary:        Swaylock, with fancy effects

License:        MIT
URL:            https://github.com/jirutka/swaylock-effects
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz

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
%autosetup -n %{name}-%{version}

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
%dir %{bash_completions_dir}
%{bash_completions_dir}/%{program_name}

%dir %{_datadir}/zsh
%dir %{zsh_completions_dir}
%{zsh_completions_dir}/_%{program_name}

%dir %{_datadir}/fish
%dir %{fish_completions_dir}
%{fish_completions_dir}/%{program_name}.fish

%changelog
%autochangelog
