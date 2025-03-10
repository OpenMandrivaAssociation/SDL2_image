%define major 0
%define api 2.0
%define libname %mklibname %{name}
%define oldlibname %mklibname %{name} 2.0 0
%define devname %mklibname %{name} -d

Summary:	Simple DirectMedia Layer 2 - image
Name:		SDL2_image
Version:	2.8.8
Release:	1
License:	Zlib
Group:		System/Libraries
Url:		https://www.libsdl.org/projects/SDL_image/index.html
Source0:	https://github.com/libsdl-org/SDL_image/releases/download/release-%{version}/SDL2_image-%{version}.tar.gz
BuildRequires:	pkgconfig(libavif)
BuildRequires:	pkgconfig(libjxl)
BuildRequires:	pkgconfig(libjpeg)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(libtiff-4)
BuildRequires:	pkgconfig(libwebp)
BuildRequires:	pkgconfig(sdl2) >= 2.0.8

%description
This is a simple library to load images of various formats as SDL2 surfaces.
This library currently supports BMP, PPM, PCX, GIF, JPEG, and PNG formats.

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Main library for %{name}
Group:		System/Libraries
%rename	%{oldlibname}

%description -n %{libname}
This package contains the library needed to run programs dynamically
linked with %{name}.

%files -n %{libname}
%{_libdir}/lib%{name}-%{api}.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Headers for developing programs that will use %{name}
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
This package contains the headers that programmers will need to develop
applications which will use %{name}.

%files -n %{devname}
%doc README.txt CHANGES.txt
%{_includedir}/SDL2/*
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/SDL2_image.pc
%{_libdir}/cmake/SDL2_image/

#----------------------------------------------------------------------------

%prep
%setup -q
rm -rf external/
touch NEWS README AUTHORS ChangeLog

%build
# (anssi) --disable-x-shared disable dlopening, so that we link to them
# dynamically instead, and thus get correct autorequires
export OBJC=%{__cc}

%configure \
	--disable-static \
	--enable-bmp \
	--enable-gif \
	--enable-jpg \
	--enable-pcx \
	--enable-png \
	--enable-pnm \
	--enable-tga \
	--enable-tif \
	--enable-xpm \
	--disable-jpg-shared \
	--disable-png-shared \
	--disable-webp-shared \
	--disable-tif-shared

sed -i 's!CC -shared!CC -shared -lm %{ldflags}!g' libtool

%make_build

%install
%make_install
