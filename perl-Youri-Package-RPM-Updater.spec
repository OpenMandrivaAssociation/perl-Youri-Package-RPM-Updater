%define upstream_name       Youri-Package-RPM-Updater
%define upstream_version    0.6.0

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1
Summary:	Update RPM packages
License:	GPL or Artistic
Group:		Development/Other
Url:		http://youri.zarb.org
Source0:	http://youri.zarb.or/download/%{upstream_name}-%{upstream_version}.tar.gz
BuildRequires:	perl(DateTime)
BuildRequires:	perl(Youri::Package::RPM)
BuildRequires:	perl(RPM)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(SVN::Client)
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
%setup -q -n %{upstream_name}-%{upstream_version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%__make test

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
