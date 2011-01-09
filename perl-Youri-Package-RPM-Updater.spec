%define module	Youri-Package-RPM-Updater

Name:		perl-%{module}
Version:	0.5.2
Release:	%mkrel 5
Summary:	Update RPM packages
License:	GPL or Artistic
Group:		Development/Other
Url:		http://youri.zarb.org
Source0:	http://youri.zarb.org/download/%{module}-%{version}.tar.gz
Patch0:		Youri-Package-RPM-Updater-0.5.2-rpm5-port.patch
BuildRequires:	perl(DateTime)
BuildRequires:	perl(RPM)
BuildRequires:	perl(Test::Exception)
# (tv) temporary disabled due to missing perl-SVN with new perl:
#BuildRequires:	perl(SVN::Client)
BuildRequires:	perl(LWP::UserAgent)
BuildRequires:	perl(Readonly)
BuildRequires:	perl(List::MoreUtils)
BuildRequires:	perl(YAML::AppConfig)
BuildRequires:	perl-version
Requires:	    perl-version
BuildArch:	    noarch
BuildRoot:	    %{_tmppath}/%{name}-%{version}

%description
YOURI stands for "Youri Offers an Upload & Repository Infrastucture". It aims
to build tools making management of a coherent set of packages easier.

This module updates rpm packages. When given an explicit new version, it
updates the spec file, and downloads new sources automatically. When not given
a new version, it just updates the spec file.

%prep
%setup -q -n %{module}-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
# (tv) temporary disabled due to missing perl-SVN with new perl:
#%__make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Youri
%{_mandir}/man3/*
