%global alt_pkg_name swaync

Name:           SwayNotificationCenter
Version:        0.12.1
Release:        %autorelease
Summary:        Notification daemon with GTK GUI

License:        GPL-3.0-or-later
URL:            https://github.com/ErikReider/SwayNotificationCenter
Source:         %{url}/archive/refs/tags/v%{version}.tar.gz

Provides:       desktop-notification-daemon
Provides:       sway-notification-center = %{version}-%{release}
Provides:       %{alt_pkg_name} = %{version}-%{release}

BuildRequires:  blueprint-compiler
BuildRequires:  cmake
BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  pkgconfig(fish)
BuildRequires:  pkgconfig(granite-7)
BuildRequires:  pkgconfig(gtk4-layer-shell-0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  sassc
BuildRequires:  scdoc
BuildRequires:  systemd
BuildRequires:  vala

Requires:       gvfs
Requires:       libnotify
Requires:       dbus
%{?systemd_requires}

%description
A simple notification daemon with a GTK gui for notifications and the control center

%package bash-completion
BuildArch:      noarch
Summary:        Bash completion files for %{name}
Provides:       %{alt_pkg_name}-bash-completion = %{version}-%{release}

Requires:       bash-completion
Requires:       %{name} = %{version}-%{release}

%description bash-completion
This package installs Bash completion files for %{name}

%package zsh-completion
BuildArch:      noarch
Summary:        Zsh completion files for %{name}
Provides:       %{alt_pkg_name}-zsh-completion = %{version}-%{release}

Requires:       zsh
Requires:       %{name} = %{version}-%{release}

%description zsh-completion
This package installs Zsh completion files for %{name}

%package fish-completion
BuildArch:      noarch
Summary:        Fish completion files for %{name}
Provides:       %{alt_pkg_name}-fish-completion = %{version}-%{release}

Requires:       fish
Requires:       %{name} = %{version}-%{release}

%description fish-completion
This package installs Fish completion files for %{name}

%prep
%autosetup -n %{name}-%{version} -p1

%build
%meson
%meson_build

%install
%meson_install

%post
%systemd_user_post swaync.service

%preun
%systemd_user_preun swaync.service

%files
%doc README.md
%{_bindir}/swaync-client
%{_bindir}/swaync
%license COPYING
%config(noreplace) %{_sysconfdir}/xdg/swaync/configSchema.json
%config(noreplace) %{_sysconfdir}/xdg/swaync/config.json
%config(noreplace) %{_sysconfdir}/xdg/swaync/style.css
%{_userunitdir}/swaync.service
%{_datadir}/dbus-1/services/org.erikreider.swaync.service
%{_datadir}/glib-2.0/schemas/org.erikreider.swaync.gschema.xml
%{_mandir}/man1/swaync-client.1*
%{_mandir}/man1/swaync.1*
%{_mandir}/man5/swaync.5*

%files bash-completion
%{bash_completions_dir}/swaync
%{bash_completions_dir}/swaync-client

%files zsh-completion
%{zsh_completions_dir}/_swaync
%{zsh_completions_dir}/_swaync-client

%files fish-completion
%{fish_completions_dir}/swaync-client.fish
%{fish_completions_dir}/swaync.fish

%changelog
%autochangelog
