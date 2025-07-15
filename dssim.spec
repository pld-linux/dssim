# NOTE: for versions >= 2 (rewritten in rust, no C library, limited archs set) see dssim2.spec
Summary:	Tool to compute (dis)similarity between two or more images
Summary(pl.UTF-8):	Narzędzie do obliczania (nie)podobieństwa dwóch lub większej liczby obrazów
Name:		dssim
Version:	1.3.3
Release:	2
License:	AGPL v3+
Group:		Applications/Graphics
#Source0Download: https://github.com/pornel/dssim/releases
Source0:	https://github.com/pornel/dssim/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	4bd83d9c553f6855da581ea6e0c41e03
Patch0:		%{name}-meson.patch
URL:		https://kornel.ski/dssim
BuildRequires:	libpng-devel
BuildRequires:	meson >= 0.35.0
BuildRequires:	ninja >= 1.5
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	zlib-devel
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This tool computes (dis)similarity between two or more PNG images
using an algorithm approximating human vision.

Comparison is done using the SSIM algorithm at multiple weighed
resolutions.

%description -l pl.UTF-8
To narzędzie oblicza (nie)podobieństwo dwóch lub większej liczby
obrazów PNG przy użyciu algorytmu przybliżającego ludzkie widzenie.

Porównywanie jest wykonywane algorytmem SSIM z wieloma ważonymi
rozdzielczościami.

%package libs
Summary:	DSSIM shared library
Summary(pl.UTF-8):	Biblioteka współdzielona DSSIM
Group:		Libraries

%description libs
DSSIM shared library to compute (dis)similarity between two or more
images.

%description libs -l pl.UTF-8
Biblioteka współdzielona DSSIM do obliczania (nie)podobieństwa dwóch
lub większej liczby obrazów.

%package devel
Summary:	Header file for DSSIM library
Summary(pl.UTF-8):	Plik nagłówkowy biblioteki DSSIM
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
Header file for DSSIM library.

%description devel -l pl.UTF-8
Plik nagłówkowy biblioteki DSSIM.

%prep
%setup -q
%patch -P0 -p1

%build
%meson

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/dssim

%files libs
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_libdir}/libdssim-lib.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libdssim-lib.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdssim-lib.so
%{_includedir}/dssim.h
%{_pkgconfigdir}/dssim.pc
