Summary:   Bumblebee Graphical User Interface
Name:      bumblebee-ui
Version:   1
Release:   20150829.b1c8e72%{?dist}.sos
License:   GPL
Group:     User Interface/Desktops
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
URL:       https://github.com/StotinkaOS/bumblebee-ui
Source0:   %{name}-%{version}.tar.gz
Requires:  bumblebee pygtk2

%description
%{Summary}.

%prep
%setup -q

%build


%install
rm -rf %{buildroot}
mkdir %{buildroot}
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/%{name}/
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/
mkdir -p %{buildroot}%{_datadir}/applications/

cp app/*.* %{buildroot}%{_datadir}/%{name}/
cp icons/*.* %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/
install -m 755 bumblebee-app-settings.desktop %{buildroot}%{_datadir}/applications/
install -m 755 bumblebee-indicator.desktop  %{buildroot}%{_datadir}/applications/
ln -s %{_datadir}/%{name}/AppSettings.py %{buildroot}%{_bindir}/bumblebee-app-settings
ln -s %{_datadir}/%{name}/Bumblebee-Indicator.py %{buildroot}%{_bindir}/bumblebee-indicator

%clean

%files
%defattr(-,root,root)
%attr(755,root,root)
%doc README
%{_datadir}/bumblebee-ui/
%{_datadir}/applications/bumblebee-app-settings.desktop
%{_datadir}/applications/bumblebee-indicator.desktop
%{_datadir}/icons/hicolor/48x48/apps/bumblebee*
%{_bindir}/bumblebee-*


%changelog
* Sat Aug 29 2015 Ivaylo Kuzev <ivo@stotinkaos.net> 
- Initial .spec for StotinkaOS 


