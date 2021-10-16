%define oname sereno-violetto
%define bdate   2021.10.18

Summary:  Sereno-violetto Plasma 5 Aurorae theme for OpenMandriva
Name:   	sereno-violetto
Version:    2.0
Release:    1
License:    GPL
Group:  Graphical desktop/KDE
Url:    https://github.com/rugyada/sereno-violetto
Source0:    sereno-violetto.tar.gz

BuildRequires:	extra-cmake-modules
BuildArch:	noarch

%description
Sereno-violetto Plasma 5 Aurorae theme for OpenMandriva Linux created by craig https://www.opendesktop.org/u/caig/

%files
%dir %{_kde5_datadir}/aurorae/themes/sereno-violetto/
%{_kde5_datadir}/aurorae/themes/sereno-violetto/*

#----------------------------------------------------------------------------

%prep
%setup -qn %{oname}

%build

%install
mkdir -p %{buildroot}%{_kde5_datadir}/aurorae/themes/sereno-violetto
cp * %{buildroot}%{_kde5_datadir}/aurorae/themes/sereno-violetto/
