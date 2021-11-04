%global debug_package %{nil}
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

# ---------------
# rhos-bootstrap
# ---------------

Name:           rhos-bootstrap
Summary:        Red Hat OpenStack bootstrap utility
Version:        XXX
Release:        XXX

Group:          System Environment/Base
License:        ASL 2.0

URL:            https://github.com/redhat-openstack/rhos-bootstrap
Source:         https://github.com/redhat-openstack/rhos-bootstrap/archive/%{upstream_version}.tar.gz#/rhos-bootstrap-%{upstream_version}.tar.gz

BuildArch:      noarch

Requires:       python3-libdnf
Requires:       python3-dnf
Requires:       python3-pyyaml
Requires:       python3-requests

Suggests:       subscription-manager

BuildRequires:  python3-pbr >= 2.0.0

%{?python_provide:%python_provide python3-%{name}}

%description
A bootstrap tool used to handle repository, dnf module configuration, and
tripleoclient installation in preparation for a Red Hat OpenStack installation.

# ---------------
# Setup
# ---------------

%prep
%autosetup -n rhos-bootstrap-%{upstream_version} -S git
rm -rf *.egg-info

# ---------------
# Build
# ---------------

%build
%{py3_build}

# ---------------
#  Install
# ---------------

%install
%{py3_install}

# ---------------
#  Misc
# ---------------

%check
# TODO(mwhahaha): run tests

%post

%preun

# ---------------
# Files
# ---------------

%files
%license LICENSE
%doc README.rst AUTHORS ChangeLog
%{python3_sitelib}/rhos_bootstrap*
%{_bindir}/%{name}
%{_datadir}/%{name}

# ---------------

%changelog
