#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : linecache2
Version  : 1.0.0
Release  : 11
URL      : https://pypi.python.org/packages/source/l/linecache2/linecache2-1.0.0.tar.gz
Source0  : https://pypi.python.org/packages/source/l/linecache2/linecache2-1.0.0.tar.gz
Summary  : Backports of the linecache module
Group    : Development/Tools
License  : Python-2.0
Requires: linecache2-python
BuildRequires : extras
BuildRequires : extras-python
BuildRequires : fixtures-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python-mimeparse-python
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : six
BuildRequires : six-python
BuildRequires : testtools
BuildRequires : testtools-python
BuildRequires : traceback2-python
BuildRequires : unittest2-python

%description
A backport of linecache to older supported Pythons.
>>> import linecache2 as linecache

%package python
Summary: python components for the linecache2 package.
Group: Default

%description python
python components for the linecache2 package.


%prep
%setup -q -n linecache2-1.0.0

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python2 setup.py test || :
%install
rm -rf %{buildroot}
python2 setup.py build -b py2 install --root=%{buildroot}
python3 setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
