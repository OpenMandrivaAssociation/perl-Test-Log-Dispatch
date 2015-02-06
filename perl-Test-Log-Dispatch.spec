%define upstream_name    Test-Log-Dispatch
%define upstream_version 0.03

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	7

Summary:	A Log::Dispatch object that keeps track of everything logged to it in memory
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Test/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(List::MoreUtils)
BuildRequires:	perl(Log::Dispatch::Array)
BuildRequires:	perl(Log::Dispatch::Output)
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

