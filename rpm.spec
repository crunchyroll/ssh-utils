# cpennello 2015-02-05 RPM specification file for ssh-utils.

%define prefix usr
%define binpath %{prefix}/bin

summary: Crunchyroll SSH Utilities
name: cr-ssh-utils
version: 1.0
release: 1
group: Development/Tools
vendor: Crunchyroll, Inc.
license: Copyright (c) 2016 Crunchyroll, Inc.
source: %{expand:%%(pwd)}
prefix: /%{prefix}

%description
The Crunchyroll SSH Utilities include programs for automating the
management of SSH agent sessions.

%prep
cp %{SOURCEURL0}/* .

%install
rm -fR %{buildroot}
mkdir -p %{buildroot}/%{binpath}
make prefix=%{buildroot}/%{prefix} install

%clean
rm -fR %{buildroot} %{_builddir}/*

%files
/%{binpath}/ssh-find-auth-sock
/%{binpath}/ssh-init-agent-session
/%{binpath}/ssh-reconnect-agent-session
/%{binpath}/ssh-check-private-keys
