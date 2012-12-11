%define upstream_name    Test-Log-Dispatch
%define upstream_version 0.03

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	A Log::Dispatch object that keeps track of everything logged to it in memory
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Test/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(List::MoreUtils)
BuildRequires:	perl(Log::Dispatch::Array)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Tester)
BuildArch:	noarch

%description
'Test::Log::Dispatch' is a 'Log::Dispatch' object that keeps track of
everything logged to it in memory, and provides convenient tests against
what has been logged.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.30.0-3mdv2011.0
+ Revision: 657844
- rebuild for updated spec-helper

* Sat Sep 25 2010 Shlomi Fish <shlomif@mandriva.org> 0.30.0-2mdv2011.0
+ Revision: 580985
- Bumped the release number
- Added a missing build dep
- import perl-Test-Log-Dispatch

