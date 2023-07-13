# Violetto theme Aurorae theme
Name:     sereno-violetto
Version:  2.0
Release:  2
Source0:  %{name}-%version.tar.gz

Summary:  Sereno-violetto Plasma 5 Aurorae theme
URL:      https://github.com/rugyada/sereno-violetto
License:  GPL
Group:    Graphical desktop/KDE

BuildRequires:  extra-cmake-modules
BuildArch:      noarch

%description
Sereno-violetto Plasma 5 Aurorae theme for OpenMandriva Linux created by craig https://www.opendesktop.org/u/caig/

%prep
%autosetup -p1

%build

%install
mkdir -p %{buildroot}%{_kde5_datadir}/aurorae/themes/sereno-violetto
cp * %{buildroot}%{_kde5_datadir}/aurorae/themes/sereno-violetto/

%files
%dir %{_kde5_datadir}/aurorae/themes/sereno-violetto/
%{_kde5_datadir}/aurorae/themes/sereno-violetto/*
