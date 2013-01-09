%define upstream_name       Youri-Package-RPM-Updater
%define upstream_version    0.6.2

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2
Summary:	Update RPM packages
License:	GPL or Artistic
Group:		Development/Other
Url:		http://youri.zarb.org
Source0:	http://youri.zarb.or/download/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(DateTime)
BuildRequires:	perl(Youri::Package::RPM)
BuildRequires:	perl(RPM)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(SVN::Client)
BuildRequires:	perl(LWP::UserAgent)
BuildRequires:	perl(Readonly)
BuildRequires:	perl(List::MoreUtils)
BuildRequires:	perl(YAML::AppConfig)
BuildRequires:	perl(version)
Requires:		perl(version)
BuildArch:		noarch

%description
YOURI stands for "Youri Offers an Upload & Repository Infrastucture". It aims
to build tools making management of a coherent set of packages easier.

This module updates rpm packages. When given an explicit new version, it
updates the spec file, and downloads new sources automatically. When not given
a new version, it just updates the spec file.

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files 
%doc Changes README
%{perl_vendorlib}/Youri
%{_mandir}/man3/*

%changelog
* Mon Feb 28 2011 Funda Wang <fwang@mandriva.org> 0.6.1-2mdv2011.0
+ Revision: 640785
- rebuild to obsolete old packages

* Sun Jan 30 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.6.1-1
+ Revision: 634185
- new version

* Sat Jan 29 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.6.0-1
+ Revision: 633929
- new version

* Sun Jan 09 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.5.2-5mdv2011.0
+ Revision: 630747
- merge rpm5 branch

* Wed Jul 21 2010 Thierry Vignaud <tv@mandriva.org> 0.5.2-3mdv2011.0
+ Revision: 556539
- temporary disable BR: perl-SVN & test suite due to missing perl-SVN with new perl
- rebuild for new perl

* Wed Dec 02 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.5.2-1mdv2010.1
+ Revision: 472562
- new version
- new version

* Sat Nov 21 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.5.0-1mdv2010.1
+ Revision: 468566
- new version

* Fri Jul 03 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.4.7-1mdv2010.0
+ Revision: 391956
- new version

* Tue Jun 02 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.4.6-1mdv2010.0
+ Revision: 382288
- new version

* Mon May 18 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.4.5-1mdv2010.0
+ Revision: 377350
- new version

* Thu May 07 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.4.4-1mdv2010.0
+ Revision: 373065
- new version

* Tue Jan 06 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.4.3-1mdv2009.1
+ Revision: 325397
- new vesion

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.4.2-2mdv2009.0
+ Revision: 268887
- rebuild early 2009.0 package (before pixel changes)

* Tue Apr 22 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.4.2-1mdv2009.0
+ Revision: 196539
- new  version

* Sun Feb 17 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.4.1-1mdv2008.1
+ Revision: 169415
- new version
- spec cleanup
- new version

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Nov 17 2007 Funda Wang <fwang@mandriva.org> 0.3.4-2mdv2008.1
+ Revision: 109318
- rebuild

* Thu Nov 01 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.3.4-1mdv2008.1
+ Revision: 104482
- new version

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.3.3-1mdv2008.0
+ Revision: 85914
- new version

* Fri Jul 27 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.3.2-1mdv2008.0
+ Revision: 56246
- new version

* Thu Jul 26 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.3.1-1mdv2008.0
+ Revision: 55811
- new version

* Thu Jul 26 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.3.0-1mdv2008.0
+ Revision: 55805
- new version

* Sun Jul 01 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.2.1-1mdv2008.0
+ Revision: 46763
- new version

* Sun Jul 01 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.2.0-1mdv2008.0
+ Revision: 46299
- new version

* Wed Apr 25 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.1.1-1mdv2008.0
+ Revision: 18364
- new version

* Mon Apr 23 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.1.0-2mdv2008.0
+ Revision: 17230
- force dependency on perl-version

* Sun Apr 22 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.1.0-1mdv2008.0
+ Revision: 17042
- Import perl-Youri-Package-RPM-Updater



* Sun Apr 22 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.1.0-1mdv2008.0
- first mdv release 
