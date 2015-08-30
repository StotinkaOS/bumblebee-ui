Summary:   Bumblebee Graphical User Interface
Name:      bumblebee-ui
Version:   1
Release:   20150830.b1c8e72%{?dist}.sos
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
mkdir -p %{buildroot}%{_sysconfdir}/xdg/autostart/

cp app/*.* %{buildroot}%{_datadir}/%{name}/
cp icons/*.* %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/
install -m 755 bumblebee-app-settings.desktop %{buildroot}%{_datadir}/applications/
install -m 755 bumblebee-indicator.desktop %{buildroot}%{_datadir}/applications/
install -m 755 bumblebee-indicator.desktop %{buildroot}%{_sysconfdir}/xdg/autostart/bumblebee-indicator.desktop
ln -s %{_datadir}/%{name}/AppSettings.py %{buildroot}%{_bindir}/bumblebee-app-settings
ln -s %{_datadir}/%{name}/Bumblebee-Indicator.py %{buildroot}%{_bindir}/bumblebee-indicator

%clean
rm -rf %{buildroot}


%post
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :


%files
%defattr(-,root,root)
%attr(755,root,root)
%doc README
%{_datadir}/bumblebee-ui/
%{_datadir}/applications/bumblebee-app-settings.desktop
%{_datadir}/applications/bumblebee-indicator.desktop
%{_datadir}/icons/hicolor/48x48/apps/bumblebee*
%{_sysconfdir}/xdg/autostart/bumblebee-indicator.desktop
%{_bindir}/bumblebee-*

%changelog
* Wed Aug 30 2015 Ivaylo Kuzev <ivo@stotinkaos.net>
- Update icon cache
- Add Bumblebee indicator to the autostart applications

* Sat Aug 29 2015 Ivaylo Kuzev <ivo@stotinkaos.net> 
- Initial .spec for StotinkaOS 


