#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-MooseX-Types-JSON
Version  : 1.00
Release  : 7
URL      : https://cpan.metacpan.org/authors/id/M/MI/MILA/MooseX-Types-JSON-1.00.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/M/MI/MILA/MooseX-Types-JSON-1.00.tar.gz
Summary  : 'JSON datatype for Moose'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-MooseX-Types-JSON-license = %{version}-%{release}
Requires: perl-MooseX-Types-JSON-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(B::Hooks::EndOfScope)
BuildRequires : perl(Carp::Clan)
BuildRequires : perl(Class::Load)
BuildRequires : perl(Class::Load::XS)
BuildRequires : perl(Data::OptList)
BuildRequires : perl(Devel::GlobalDestruction)
BuildRequires : perl(Devel::OverloadInfo)
BuildRequires : perl(Devel::StackTrace)
BuildRequires : perl(Eval::Closure)
BuildRequires : perl(JSON)
BuildRequires : perl(MRO::Compat)
BuildRequires : perl(Module::Implementation)
BuildRequires : perl(Module::Runtime)
BuildRequires : perl(Moose)
BuildRequires : perl(Moose::Util::TypeConstraints)
BuildRequires : perl(MooseX::Types)
BuildRequires : perl(Package::DeprecationManager)
BuildRequires : perl(Package::Stash)
BuildRequires : perl(Params::Util)
BuildRequires : perl(Sub::Exporter)
BuildRequires : perl(Sub::Exporter::ForMethods)
BuildRequires : perl(Sub::Exporter::Progressive)
BuildRequires : perl(Sub::Identify)
BuildRequires : perl(Sub::Install)
BuildRequires : perl(Sub::Name)
BuildRequires : perl(Try::Tiny)
BuildRequires : perl(namespace::autoclean)
BuildRequires : perl(namespace::clean)

%description
This archive contains the distribution MooseX-Types-JSON,
version 1.00:
JSON datatype for Moose

%package dev
Summary: dev components for the perl-MooseX-Types-JSON package.
Group: Development
Provides: perl-MooseX-Types-JSON-devel = %{version}-%{release}
Requires: perl-MooseX-Types-JSON = %{version}-%{release}

%description dev
dev components for the perl-MooseX-Types-JSON package.


%package license
Summary: license components for the perl-MooseX-Types-JSON package.
Group: Default

%description license
license components for the perl-MooseX-Types-JSON package.


%package perl
Summary: perl components for the perl-MooseX-Types-JSON package.
Group: Default
Requires: perl-MooseX-Types-JSON = %{version}-%{release}

%description perl
perl components for the perl-MooseX-Types-JSON package.


%prep
%setup -q -n MooseX-Types-JSON-1.00
cd %{_builddir}/MooseX-Types-JSON-1.00

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test || :

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-MooseX-Types-JSON
cp %{_builddir}/MooseX-Types-JSON-1.00/LICENSE %{buildroot}/usr/share/package-licenses/perl-MooseX-Types-JSON/d7d164eebbac5ca055935f48ffcfaac6ab44138c
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/MooseX::Types::JSON.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-MooseX-Types-JSON/d7d164eebbac5ca055935f48ffcfaac6ab44138c

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/MooseX/Types/JSON.pm
