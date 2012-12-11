%define upstream_name    File-ShareDir-PathClass
%define upstream_version 1.101620

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    File::ShareDir returning Path::Class objects
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/File/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Carp)
BuildRequires: perl(English)
BuildRequires: perl(File::Find)
BuildRequires: perl(File::ShareDir)
BuildRequires: perl(File::Temp)
BuildRequires: perl(Module::Build)
BuildRequires: perl(Path::Class)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Sub::Exporter)
BuildRequires: perl(Test::More)
BuildRequires: perl(Module::Build)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This module is just a wrapper around the File::ShareDir manpage functions,
transforming their return value to the Path::Class manpage objects. This
allows for easier usage of the value.

Refer to the File::ShareDir manpage (section FUNCTIONS) for a list of which
functions are supported.

'File::ShareDir::PathClass' supports both a procedural and a clas methods
API.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Build.PL installdirs=vendor

./Build

%check
./Build test

%install
rm -rf %buildroot
./Build install destdir=%{buildroot}

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes LICENSE META.yml README
%{_mandir}/man3/*
%perl_vendorlib/*




%changelog
* Fri Jun 17 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.101.620-1mdv2011.0
+ Revision: 685754
- import perl-File-ShareDir-PathClass

