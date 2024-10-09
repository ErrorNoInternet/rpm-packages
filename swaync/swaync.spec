%global alt_pkg_name swaync

Name:           SwayNotificationCenter
Version:        0.10.1
Release:        %autorelease
Summary:        Notification daemon with GTK GUI
Provides:       desktop-notification-daemon
Provides:       sway-notification-center = %{version}-%{release}
Provides:       %{alt_pkg_name} = %{version}-%{release}
License:        GPL-3.0-or-later

URL:            https://github.com/ErikReider/SwayNotificationCenter
Source:         %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  meson >= 0.51.0
BuildRequires:  vala >= 0.56
BuildRequires:  scdoc
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22
BuildRequires:  pkgconfig(gtk-layer-shell-0) >= 0.1
BuildRequires:  pkgconfig(json-glib-1.0) >= 1.0
BuildRequires:  pkgconfig(libhandy-1) >= 1.4.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.50
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 1.68
BuildRequires:  pkgconfig(gee-0.8) >= 0.20
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  pkgconfig(fish)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(granite)
BuildRequires:  systemd-devel
BuildRequires:  systemd
BuildRequires:  sassc
BuildRequires:  granite-devel

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
