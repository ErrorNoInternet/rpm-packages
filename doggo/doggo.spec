# Generated by go2rpm 1.13.1
%bcond_without check

# https://github.com/mr-karan/doggo
%global goipath         github.com/mr-karan/doggo
Version:                1.0.4

%gometa -L -f

%global common_description %{expand:
:dog: Command-line DNS Client for Humans. Written in Golang.}

%global golicenses      LICENSE
%global godocs          docs README.md TODO.md www/api/api.md

Name:           doggo
Release:        %autorelease
Summary:        :dog: Command-line DNS Client for Humans. Written in Golang

License:        GPL-3.0-only
URL:            %{gourl}
Source:         %{gosource}

BuildRequires:  git

%description %{common_description}

%gopkg

%prep
%goprep -A
%autopatch -p1
go mod vendor

%build
for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done
for cmd in web; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

chmod -R u+w %{gobuilddir}/pkg

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE
%doc docs README.md TODO.md www/api/api.md
%{_bindir}/*

%gopkgfiles

%changelog
%autochangelog