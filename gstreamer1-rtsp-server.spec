%global         majorminor      1.0

Name:           gstreamer1-rtsp-server
Version:        1.14.5
Release:        1%{?dist}
Summary:        GStreamer RTSP server library
License:        LGPLv2+
URL:            http://gstreamer.freedesktop.org/

Source0:        http://gstreamer.freedesktop.org/src/gst-rtsp/gst-rtsp-server-%{version}.tar.xz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gobject-introspection-devel
BuildRequires:  gstreamer1-devel >= %{version}
BuildRequires:  gstreamer1-plugins-base-devel >= %{version}
BuildRequires:  gtk-doc >= 1.3
BuildRequires:  libtool

Requires:       gstreamer1%{?_isa} >= %{version}
Requires:       gstreamer1-plugins-base%{?_isa} >= %{version}

%description
A GStreamer-based RTSP server library.

%package devel
Summary:        Development files for %{name}
Requires:       gstreamer1-devel%{?_isa} >= %{version}
Requires:       gstreamer1-plugins-base-devel%{?_isa} >= %{version}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for %{name}, the GStreamer RTSP server library.

%package devel-docs
Summary:         Developer documentation for GStreamer-based RTSP server library
Requires:        %{name} = %{version}-%{release}
BuildArch:       noarch

%description devel-docs
This %{name}-devel-docs contains developer documentation for the
GStreamer-based RTSP server library.

%prep
%autosetup -p1 -n gst-rtsp-server-%{version}
sed -i -e 's/-Wno-portability 1.14/-Wno-portability 1.13/g' configure.ac

%build
autoreconf -fiv
%configure \
    --enable-gtk-doc \
    --disable-fatal-warnings \
    --disable-static \
    --disable-tests

%make_build V=1

%check
make check

%install
%make_install

find %{buildroot} -name '*.la' -delete

%ldconfig_scriptlets

%files
%license COPYING.LIB
%doc README TODO NEWS
%dir %{_libdir}/girepository-1.0/
%{_libdir}/libgstrtspserver-%{majorminor}.so.*
%{_libdir}/girepository-1.0/GstRtspServer-%{majorminor}.typelib

%files devel
%dir %{_datadir}/gir-1.0/
%{_includedir}/gstreamer-%{majorminor}/gst/rtsp-server
%{_libdir}/libgstrtspserver-%{majorminor}.so
%{_libdir}/pkgconfig/gstreamer-rtsp-server-%{majorminor}.pc
%{_datadir}/gir-1.0/GstRtspServer-%{majorminor}.gir
%{_libdir}/gstreamer-%{majorminor}/libgstrtspclientsink.so

%files devel-docs
%doc %{_datadir}/gtk-doc/html/gst-rtsp-server-%{majorminor}
%dir %{_datadir}/gtk-doc/
%dir %{_datadir}/gtk-doc/html/

%changelog
* Mon Jul 13 2020 Simone Caronni <negativo17@gmail.com> - 1.14.5-1
- Update to 1.14.5.

* Mon Nov 11 2019 Simone Caronni <negativo17@gmail.com> - 1.14.4-1
- Rebase to 1.14.4.

