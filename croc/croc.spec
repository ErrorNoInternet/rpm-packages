%global goipath         github.com/schollz/croc
Version:                10.2.3

%gometa -L -f

%global goaltipaths     github.com/schollz/croc/v10

%global common_description %{expand:
croc is a tool that allows any two computers to simply and securely transfer
files and folders.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           croc
Release:        %autorelease
Summary:        Easily and securely send things from one computer to another

License:        MIT
URL:            %{gourl}
Source:         %{gosource}

BuildRequires:  systemd-rpm-macros
BuildRequires:  git

%description %{common_description}

%gopkg

%prep
%goprep -A
%autopatch -p1
go mod vendor

%build
%gobuild -o %{gobuilddir}/bin/croc %{goipath}

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

install -Dpm0644 -t %{buildroot}%{_unitdir} croc.service
install -Dpm0644 src/install/bash_autocomplete \
                 %{buildroot}%{bash_completions_dir}/croc
install -Dpm0644 src/install/zsh_autocomplete \
                 %{buildroot}%{zsh_completions_dir}/_croc

chmod -R u+w %{gobuilddir}/pkg

%post
%systemd_post croc.service

%preun
%systemd_preun croc.service

%postun
%systemd_postun_with_restart croc.service

%files
%license LICENSE
%license vendor/modules.txt
%doc README.md
%{_bindir}/*
%{bash_completions_dir}/croc
%{zsh_completions_dir}/_croc
%{_unitdir}/croc.service

%gopkgfiles

%changelog
%autochangelog
