%define major 0
%define api 2.0
%define libname %mklibname %{name} %{api} %{major}
%define devname %mklibname %{name} -d

Summary:	Simple DirectMedia Layer 2 - image
Name:		SDL2_image
Version:	2.0.0
Release:	4
License:	Zlib
Group:		System/Libraries
Url:		http://www.libsdl.org/projects/SDL_image/index.html
Source0:	http://www.libsdl.org/projects/SDL_image/release/%{name}-%{version}.tar.gz
BuildRequires:	jpeg-devel
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(libtiff-4)
BuildRequires:	pkgconfig(libwebp)
BuildRequires:	pkgconfig(sdl2) >= 2.0.3

%description
This is a simple library to load images of various formats as SDL2 surfaces.
This library currently supports BMP, PPM, PCX, GIF, JPEG, and PNG formats.

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Main library for %{name}
Group:		System/Libraries

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
%doc README.txt CHANGES.txt COPYING.txt
%{_includedir}/SDL2/*
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/SDL2_image.pc

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%configure2_5x \
	--disable-static \
	--enable-bmp \
	--enable-gif \
	--enable-jpg \
	--enable-pcx \
	--enable-png \
	--enable-tif \
	--enable-xpm \
	--disable-jpg-shared \
	--disable-png-shared \
	--disable-tif-shared

%make

%install
%makeinstall_std

