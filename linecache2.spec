#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x89EFD588E975D6DF (rbtcollins@hp.com)
#
Name     : linecache2
Version  : 1.0.0
Release  : 63
URL      : http://pypi.debian.net/linecache2/linecache2-1.0.0.tar.gz
Source0  : http://pypi.debian.net/linecache2/linecache2-1.0.0.tar.gz
Source1  : http://pypi.debian.net/linecache2/linecache2-1.0.0.tar.gz.asc
Summary  : Backports of the linecache module
Group    : Development/Tools
License  : Python-2.0
Requires: linecache2-python = %{version}-%{release}
Requires: linecache2-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : fixtures-python
BuildRequires : pbr
BuildRequires : testtools
BuildRequires : testtools-python
BuildRequires : unittest2
BuildRequires : unittest2-python

%description
>>> import linecache2 as linecache
        
        Profit.

%package python
Summary: python components for the linecache2 package.
Group: Default
Requires: linecache2-python3 = %{version}-%{release}

%description python
python components for the linecache2 package.


%package python3
Summary: python3 components for the linecache2 package.
Group: Default
Requires: python3-core
Provides: pypi(linecache2)

%description python3
python3 components for the linecache2 package.


%prep
%setup -q -n linecache2-1.0.0
cd %{_builddir}/linecache2-1.0.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1603394959
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test || :
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
