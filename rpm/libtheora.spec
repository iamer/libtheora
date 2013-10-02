Name:       libtheora
Summary:    Theora Video Compression Codec
Version:    1.1.1
Release:    1
Group:      System/Libraries
License:    BSD
URL:        http://www.theora.org/
Source0:    http://downloads.xiph.org/releases/theora/%{name}-%{version}.tar.bz2
Requires(post):  /sbin/ldconfig
Requires(postun):  /sbin/ldconfig
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(libpng)

BuildRoot:  %{_tmppath}/%{name}-%{version}-build

%description
Description: %{summary}


%package devel
Summary:    Development tools for Theora applications
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
Description: %{summary}


%prep
%setup -q -n %{name}-%{version}/theora

%build
./autogen.sh
%configure --disable-static \
    --enable-shared \
    --disable-sdltest \
    --disable-examples

# Call make instruction with smp support
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install

%clean
rm -rf %{buildroot}



%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig



%files
%defattr(-,root,root,-)
%doc README COPYING
%{_libdir}/libtheora.so.*
%{_libdir}/libtheoradec.so.*
%{_libdir}/libtheoraenc.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/theora
%{_libdir}/*.so
%{_libdir}/pkgconfig/theora.pc
%{_libdir}/pkgconfig/theoraenc.pc
%{_libdir}/pkgconfig/theoradec.pc
