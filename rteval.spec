# TODO: loads (see rteval-loads.spec), server parts (see server/rteval-parser.spec)
Summary:	Utility to evaluate system suitability for RT Linux
Summary(pl.UTF-8):	Narzędzie do szacowania przydatkości systemu dla Linuksa RT
Name:		rteval
Version:	3.2
Release:	0.1
License:	GPL v2
Group:		Applications/System
Source0:	https://www.kernel.org/pub/linux/utils/rteval/%{name}-%{version}.tar.xz
# Source0-md5:	36203a51a017d6c014ea45099dd62f67
URL:		https://wiki.linuxfoundation.org/realtime/documentation/howto/tools/rteval
BuildRequires:	python3 >= 1:3.2
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	numactl
Requires:	python3-ethtool
Requires:	python3-libxml2
Requires:	python3-lxml
Requires:	python3-modules >= 1:3.2
Requires:	python3-schedutils
Requires:	rt-tests >= 0.97
Requires:	sysstat
Requires:	trace-cmd
# TODO:
#Requires:	python3-dmidecode >= 3.10
#Requires:	rteval-loads >= 1.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The rteval script is a utility for measuring various aspects of
realtime behavior on a system under load. The script unpacks the
kernel source, and then goes into a loop, running hackbench and
compiling a kernel tree. During that loop the cyclictest program is
run to measure event response time. After the run time completes, a
statistical analysis of the event response times is done and printed
to the screen.

%description -l pl.UTF-8
Skrypt rteval to narzędzie mierzące różne aspekty zachowania czasu
rzeczywistego w systemie pod obciążeniem. Skrypt rozpakowuje źródła
jądra, a następnie wchodzi w pętlę, uruchamiając hackbench i
kompilację jądra. W trakcie tej pętli uruchamiany jest program
cyclictest, mierzący czas reakcji na zdarzenia. Po zakończeniu
działania jest wykonywana i wypisywana analiza statystyczna czasów
reakcji.

%prep
%setup -q

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO
%attr(755,root,root) %{_bindir}/rteval
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/rteval.conf
%{py3_sitescriptdir}/rteval
%{py3_sitescriptdir}/rteval-%{version}-py*.egg-info
%{_datadir}/rteval
%{_mandir}/man8/rteval.8*
