%define		_state		unstable
%define		orgname		kdegames
%define		qtver		4.6.1

Summary:	K Desktop Environment - games
Summary(es.UTF-8):	K Desktop Environment - Juegos
Summary(ja.UTF-8):	KDEデスクトップ環境 - ゲーツ1�7
Summary(ko.UTF-8):	K 데스크탑 환경 - 놄1�7을1�7게임)
Summary(pl.UTF-8):	K Desktop Environment - gry
Summary(pt_BR.UTF-8):	K Desktop Environment - Jogos
Summary(zh_CN.UTF-8):	KDE游戏
Name:		kde4-kdegames
Version:	4.3.98
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.bz2
# Source0-md5:	a44baaaeae4e8921db522c38723caeb9
BuildRequires:	Qt3Support-devel >= %{qtver}
BuildRequires:	QtNetwork-devel >= %{qtver}
BuildRequires:	QtOpenGL-devel >= %{qtver}
BuildRequires:	QtSvg-devel >= %{qtver}
BuildRequires:	QtTest-devel >= %{qtver}
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	cmake >= 2.8.0
BuildRequires:	ggz-client-libs-devel
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	qca-devel >= 2.0.1
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libraries for kdegames which contain highscore support functions.

%description -l pl.UTF-8
Biblioteki dla gier KDE zawierające wsparcie dla tabel wyników.

%package devel
Summary:	Development files for KDE games
Summary(pl.UTF-8):	Pliki przydatne twórcom gier dla KDE
Summary(pt_BR.UTF-8):	Arquivos de inclusão do kdegames
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-ksirk = %{version}-%{release}
Requires:	kde4-kdelibs-devel >= %{version}

%description devel
Development files for KDE games.

%description devel -l pl.UTF-8
Pliki dla programistów KDE games.

%description devel -l pt_BR.UTF-8
Este pacote detém os arquivos de inclusão necessários para compilar
aplicativos que usam bibliotecas do kdegames.

%package bovo
Summary:	bovo
Summary(pl.UTF-8):	bovo
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}
Requires:	kde4-kdebase >= %{version}

%description bovo
bovo.

%description bovo -l pl.UTF-8
bovo.

%package carddecks
Summary:	KDE carddecks
Summary(pl.UTF-8):	Karcianki dla KDE
Summary(pt_BR.UTF-8):	Biblioteca de baralhos para jogos do KDE que usem cartas
Group:		X11/Applications/Games
Requires:	kde4-kdelibs >= %{version}

%description carddecks
Backgrounds for carddecks in KDE card games.

%description carddecks -l pl.UTF-8
Tła dla talii kart w karcianki pod KDE.

%description carddecks -l pt_BR.UTF-8
Biblioteca de baralhos para jogos do KDE que usem cartas.

%package kfourinline
Summary:	kfourinline
Summary(pl.UTF-8):	kfourinline
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}
Requires:	kde4-kdebase >= %{version}

%description kfourinline
kfourinline.

%description kfourinline -l pl.UTF-8
kfourinline.

%package katomic
Summary:	KDE Sokoban clone
Summary(pl.UTF-8):	Klon gry Sokoban dla KDE
Summary(pt_BR.UTF-8):	Jogo semelhante ao Sokoban mas o objetivo é formar moléculas
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description katomic
Atomic Entertainment is a small game which resembles Sokoban. The
Object of the game is to build chemical molecules on a Sokoban like
board.

%description katomic -l pl.UTF-8
Atomic to mała gra podobna do gry Sokoban. Celem gry jest zbudowanie
cząsteczek chemicznych na planszy podobnej do tej z gry Sokoban.

%description katomic -l pt_BR.UTF-8
Jogo semelhante ao Sokoban mas o objetivo é formar moléculas.

%package kiriki
Summary:	kiriki
Summary(pl.UTF-8):	kiriki
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description kiriki
kiriki.

%description kiriki -l pl.UTF-8
kiriki.

%package kbattleship
Summary:	Battleship for KDE
Summary(pl.UTF-8):	Statki dla KDE
Summary(pt_BR.UTF-8):	Jogo de batalha naval com servidor embutido
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description kbattleship
Battleship for KDE.

%description kbattleship -l pl.UTF-8
Statki dla KDE.

%description kbattleship -l pt_BR.UTF-8
Jogo de batalha naval com servidor embutido.

%package kblackbox
Summary:	A little logical game for KDE
Summary(pl.UTF-8):	Prosta gra logiczna
Summary(pt_BR.UTF-8):	Versão do jogo Blackbox do Emacs para KDE
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description kblackbox
KBlackbox is a game of hide and seek played on an grid of boxes. Your
opponent (the Random number generator, in this case) has hidden
several balls within this box. By shooting rays into the box and
observing where they emerge it is possible to deduce the positions of
the hidden balls. The fewer rays you use to find the balls, the better
(the lower) your score.

%description kblackbox -l pl.UTF-8
KBlackbox to gra w ukrywanie i szukanie rozgrywana na siatce pudełek.
Przeciwnik (w tym wypadku generator liczb losowych) ukrył kilka piłek
w tym pudełku. Poprzez strzelanie promieniami w pudełko i obserwowanie
jak się wynurzają można wydedukować położenie ukrytych piłek. Im mniej
promieni użyje się do znalezienia piłek, tym lepszy (mniejszy) jest
wynik.

%description kblackbox -l pt_BR.UTF-8
Versão do jogo Blackbox do Emacs para KDE.

%package kbounce
Summary:	Claim areas and don't get disturbed
Summary(pl.UTF-8):	Gra polegająca na pozyskiwaniu terenu wbrew przeciwnikom
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description kbounce
Claim areas and don't get disturbed.

%description kbounce -l pl.UTF-8
Gra polegająca na pozyskiwaniu terenu wbrew przeciwnikom.

%package kgoldrunner
Summary:	A KDE clone of Lode Runner (TM) Commodore game
Summary(pl.UTF-8):	Klon gry Lode Runner dla KDE
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description kgoldrunner
KGoldrunner is based on the Lode Runner (TM) game written in the USA
by Doug Smith in 1983 for the Apple II and Commodore 64 computers.

%description kgoldrunner -l pl.UTF-8
KGoldrunner jest oparty na grze Lode Runner (TM) napisanej w 1983 w
USA przez Douga Smitha na komputery Apple II i Commodore 64.

%package kjumpingcube
Summary:	A little tactical game for KDE
Summary(pl.UTF-8):	Prosta gra taktyczna dla KDE
Summary(pt_BR.UTF-8):	Jogo de estratégia para 2 contendores
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description kjumpingcube
KJumpingCube is a simple tactical game. You can play it against the
computer or against the friend. The playing field consists of squares
that contains points. By clicking on the squares you can increase the
points, and if the points reach a maximum the points will jump to the
squares neighbours and take them over. Winer is the one, who owns all
squares.

%description kjumpingcube -l pl.UTF-8
KJumpingCube to prosta gra taktyczna. Można w nią grać przeciwko
komputerowi lub przeciwko koledze. Plansza do gry zawiera pola, które
zawierają punkty. Przez klikanie na pola zwiększa się liczbę punktów
na nich. Gdy liczba punktów na określonym polu osiągnie maksymalną
wartość, punkty przeskakują na sąsiednie pola przejmując je tym samym
na własność. Zwycięzca jest jeden - to ten, kto przejmie wszystkie
pola na własność.

%description kjumpingcube -l pt_BR.UTF-8
Jogo de estratégia para 2 contendores.

%package klines
Summary:	Lines for KDE
Summary(pl.UTF-8):	Gra Lines dla KDE
Group:		X11/Applications/Games
Requires:	%{name} = :%{version}-%{release}

%description klines
Lines for KDE. The main rules of game is as simple as possible: you
move (using mouse) marbles from cell to cell and build lines
(horizontal, vertical or diagonal). When a line contains 5 or more
marbles - they are removed from the field and your score grows. After
each of your turns computer drops three more marbles onto the field.

%description klines -l pl.UTF-8
Gra Lines dla KDE. Podstawowe zasady gry są najprostsze jak to
możliwe: przesuwa się (przy użyciu muszy) klocki z pola na pole i
buduje linie (poziome, pionowe lub ukośne). Kiedy linia zawiera 5 lub
więcej klocków - są usuwane z pola i wynik wzrasta. Po każdym ruchu
gracza komputer zrzuca trzy dodatkowe klocki.

%package kmahjongg
Summary:	KDE Mahjongg clone
Summary(pl.UTF-8):	Klon gry Mahjongg dla KDE
Summary(pt_BR.UTF-8):	Versão do jogo Mahjongg para o KDE
Group:		X11/Applications/Games
Requires:	%{name} = :%{version}-%{release}

%description kmahjongg
This program is a clone of the well known Mahjongg game.

%description kmahjongg -l pl.UTF-8
Wersja KDE znanej gry Mahjongg.

%description kmahjongg -l pt_BR.UTF-8
Versão do jogo Mahjongg para o KDE.

%package kmines
Summary:	KDE minesweeper game
Summary(pl.UTF-8):	Saper dla KDE
Summary(pt_BR.UTF-8):	Versão do jogo 'caça-minas' para o KDE
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description kmines
This is a very classical minesweeper written from scratch.
- 3 predefined levels (Easy: 8x8 with 10 mines, Normal: 16x16 with 40
  mines, Expert: 30x16 with 99 mines)
- Custom levels
- High Scores.

%description kmines -l pl.UTF-8
Wersja klasycznej gry "saper" dla KDE, napisana od zera. Cechy:
- 3 predefiniowane poziomy (łatwy - 8x8 z 10 minami, normalny - 16x16
  z 40 minami, dla ekspertów - 30x16 z 99 minami)
- definiowalne poziomy
- lista najlepszych wyników.

%description kmines -l pt_BR.UTF-8
Versão do jogo 'caça-minas' para o KDE.

%package knetwalk
Summary:	KDE knetwalk
Summary(pl.UTF-8):	knetwalk dla KDE
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description knetwalk
The aim of this game is to connect the network with a minimum amount
of clicks.

%description knetwalk -l pl.UTF-8
Celem tej gry jest połączenie sieci minimalną liczbą kliknięć.

%package kolf
Summary:	Miniature golf for KDE
Summary(pl.UTF-8):	Mini golf
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description kolf
Kolf is a miniature golf game with block graphics and a 2D top-down
view. Courses are dynamic, and up to 10 people can play at once in
competition.

%description kolf -l pl.UTF-8
Kolf to miniaturowa gra w golfa z blokowa grafiką i dwuwymiarowym
widokiem. Rundy są dynamiczne, a w zawodach może grać do 10 osób
naraz.

%package konquest
Summary:	KDE version of Gnu-Lactic Konquest
Summary(pl.UTF-8):	Podbój galaktyki - wersja KDE gry Gnu-Lactic Konquest
Summary(pt_BR.UTF-8):	Jogo espacial de estratégia
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description konquest
This the KDE version of Gnu-Lactic Konquest, a multi-player strategy
game. The goal of the game is to expand your interstellar empire
across the galaxy and of course, crush your rivals in the process.

%description konquest -l pl.UTF-8
To jest wersja KDE gry Gnu-Lactic Konquest - gry strategicznej dla
wielu graczy. Celem gry jest rozszerzenie imperium międzygwiezdnego
poprzez galaktyki, i oczywiście niszczenie w tym czasie przeciwników.

%description konquest -l pt_BR.UTF-8
Jogo espacial de estratégia.

%package kpat
Summary:	KDE solitaire patience game
Summary(pl.UTF-8):	Pasjanse dla KDE
Summary(pt_BR.UTF-8):	Versão do jogo 'Paciência' para o KDE
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-carddecks = %{version}-%{release}

%description kpat
KDE solitaire patience games.

%description kpat -l pl.UTF-8
Program dla KDE umożliwiający układanie kilku rodzajów pasjansów.

%description kpat -l pt_BR.UTF-8
Versão do jogo 'Paciência' para o KDE.

%package kreversi
Summary:	KDE Reversi game
Summary(pl.UTF-8):	Gra Reversi dla KDE
Summary(pt_BR.UTF-8):	Jogo no estilo Otelo para KDE
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description kreversi
Reversi is a simple strategy game that is played by two players. There
is only one type of piece - one side of it is black, the other white.
If a player captures a piece on the board, that piece is turned and
belongs to that player. The winner is the person that has more pieces
of his own color on the board and if there are no more moves possible.

%description kreversi -l pl.UTF-8
Reversi to prosta gra strategiczna dla dwóch graczy. Jest tylko jeden
rodzaj pionu - z jednej strony czarny, z drugiej biały. Jeśli gracz
schwyta pion na planszy, jest on obracany i należy do tego gracza.
Zwycięzcą jest osoba, która ma na planszy więcej pionów w swoim
kolorze w chwili, gdy nie można już wykonać żadnego ruchu.

%description kreversi -l pt_BR.UTF-8
Jogo no estilo Otelo para KDE.

%package ksame
Summary:	KDE SameGame
Summary(pl.UTF-8):	"To Samo" dla KDE
Summary(pt_BR.UTF-8):	Jogo relaxante onde você deve remover o maior número possível de bolas
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description ksame
KSame is a simple game. It's played by one player, so there is only
one winner :-) You play for fun and against the highscore. It has been
inspired by SameGame, that is only famous on the Macintosh platform.

%description ksame -l pl.UTF-8
KSame to prosta gra dla jednego gracza. Można grać dla zabawy i dla
wyniku. Gra jest zainspirowana grą SameGame, słynną tylko na
Macintoshach.

%description ksame -l pt_BR.UTF-8
Jogo relaxante onde você deve remover o maior número possível de
bolinhas.

%package kshisen
Summary:	KDE Shisen-Sho
Summary(pl.UTF-8):	Shisen-Sho dla KDE
Summary(pt_BR.UTF-8):	Jogo Shisen para o KDE
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description kshisen
Shisen-Sho is similar to Mahjongg and uses the same set of tiles as
KMahjongg. The object of the game is to remove all tiles from the
field.

%description kshisen -l pl.UTF-8
Shisen-Sho to gra podobna do Mahjongg i wykorzystująca ten sam zestaw
kostek. Celem gry jest usunięcie wszystkich kostek z planszy.

%description kshisen -l pt_BR.UTF-8
Jogo Shisen para o KDE.

%package ksquares
Summary:	Kksquares
Summary(pl.UTF-8):	ksquares
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description ksquares
ksquares.

%description ksquares -l pl.UTF-8
ksquares.

%package ksudoku
Summary:	ksudoku
Summary(pl.UTF-8):	ksudoku
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description ksudoku
ksudoku.

%description ksudoku -l pl.UTF-8
ksudoku.

%package kspaceduel
Summary:	KDE space arcade game for two players
Summary(pl.UTF-8):	Gra zręcznościowa pod KDE dla dwóch graczy
Summary(pt_BR.UTF-8):	Versão do jogo Duelo Espacial para o KDE
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description kspaceduel
Each player control a ship that flies around the sun and tries to
shoot at the other ship. You can play KSpaceduel with another person,
against the computer, or you can have the computer control both ships
and play each other.

%description kspaceduel -l pl.UTF-8
Każdy z graczy kieruje statkiem, który lata dookoła słońca i próbuje
zestrzelić drugi statek. Można grać w KSpaceduel z inną osobą, z
komputerem, lub pozwolić, aby komputer kierował obydwoma statkami.

%description kspaceduel -l pt_BR.UTF-8
Versão do jogo Duelo Espacial para o KDE.

%package ktuberling
Summary:	KDE game for small children
Summary(pl.UTF-8):	Gra dla małych dzieci
Summary(pt_BR.UTF-8):	Jogo de desenho do 'Homem-batata' para crianças
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description ktuberling
It is a potato editor. That means that you can drag and drop eyes,
mouths, moustache, and other parts of face and goodies onto a
potato-like guy.

There is no winer. The only purpose is to make the funniest faces you
can.

%description ktuberling -l pl.UTF-8
KTuberling to edytor ziemniaków. Oznacza to, że można układać oczy,
usta, wąsy oraz inne części twarzy na postać podobną do ziemniaka.

W grze nie ma zwycięzcy. Jedynym celem gry jest stworzenie
najzabawniejszej twarzy, jaką się da ułożyć.

%description ktuberling -l pt_BR.UTF-8
Jogo de desenho do 'Homem-batata' para crianças.

%package lskat
Summary:	KDE lskat
Summary(pl.UTF-8):	Lskat dla KDE
Summary(pt_BR.UTF-8):	Jogo de cartas Lieutenant Skat para KDE
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-carddecks = %{version}-%{release}

%description lskat
Lieutenant skat (from German Offiziersskat) is a card game for two
players. It is roughly played according to the rules of Skat but with
only two players and simplified rules. Every player has a set of cards
in front of him/her, half of them covered and half of them open. Both
players try to win more than 60 of the 120 possible points. After 16
moves all cards are played and the game ends.

%description lskat -l pl.UTF-8
Lieutenant skat (oficerski skat, od niemieckiego Offizierskat) to gra
karciana dla dwóch graczy. Jest rozgrywana z grubsza na zasadach
skata, ale tylko między dwoma graczami i z uproszczonymi zasadami.
Każdy gracz ma zestaw kart przed sobą, z których połowa jest zakryta,
a połowa odkryta. Obaj gracze próbują wygrać ponad 60 ze 120 możliwych
punktów. Po 16 ruchach wszystkie karty są rozegrane i gra się kończy.

%description lskat -l pt_BR.UTF-8
Jogo de cartas Lieutenant Skat para KDE

%package kblocks
Summary:	KBlocks
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description kblocks
KBlocks.

%package kbreakout
Summary:	KBreakout
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description kbreakout
KBreakout.

%package kdiamond
Summary:	KDiamond
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description kdiamond
KDiamond.

%package kollision
Summary:	Kollision
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description kollision
Kollision.

%package ksirk
Summary:	KSirk
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description ksirk
KSirk.

%package kubrick
Summary:	kubrick
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description kubrick
Kubrick.

%package kapman
Summary:	kapman
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description kapman
Kapman.

%package killbots
Summary:	killbots
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description killbots
Killbots.

%package bomber
Summary:	bomber
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description bomber
Bomber.

%package kdesnake
Summary:	Kdesnake
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description kdesnake
Kdesnake.

%package ktron
Summary:	Ktron
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description ktron
Ktron.

%package granatier
Summary:	Granatier
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description granatier
Granatier.

%package kigo
Summary:	Kigo
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description kigo
Kigo.

%package palapeli
Summary:	Palapeli
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description palapeli
Palapeli.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DLIB_INSTALL_DIR=%{_libdir} \
	-DSYSCONF_INSTALL_DIR=%{_sysconfdir} \
	-DCMAKE_BUILD_TYPE=%{!?debug:Release}%{?debug:Debug} \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64 \
%endif
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

install -d $RPM_BUILD_ROOT/var/games
touch $RPM_BUILD_ROOT/var/games/kbounce.scores
# remove locolor icons
rm -rf $RPM_BUILD_ROOT%{_iconsdir}/locolor

%find_lang bomber	--with-kde
%find_lang bovo		--with-kde
%find_lang kfourinline	--with-kde
%find_lang katomic	--with-kde
%find_lang kiriki	--with-kde
%find_lang kbattleship	--with-kde
%find_lang kblackbox	--with-kde
%find_lang kbounce	--with-kde
%find_lang knetwalk	--with-kde
%find_lang kgoldrunner	--with-kde
%find_lang kjumpingcube	--with-kde
%find_lang klines	--with-kde
%find_lang kmahjongg	--with-kde
%find_lang kmines	--with-kde
%find_lang kolf		--with-kde
%find_lang konquest	--with-kde
%find_lang kpat		--with-kde
%find_lang kreversi	--with-kde
%find_lang ksame	--with-kde
%find_lang kshisen	--with-kde
%find_lang ksquares	--with-kde
%find_lang ksudoku	--with-kde
%find_lang kspaceduel	--with-kde
%find_lang ktuberling	--with-kde
%find_lang lskat	--with-kde
%find_lang kblocks	--with-kde
%find_lang kbreakout	--with-kde
%find_lang kdiamond	--with-kde
%find_lang kollision	--with-kde
%find_lang ksirk	--with-kde
%find_lang kubrick	--with-kde
%find_lang kapman	--with-kde
%find_lang killbots	--with-kde
#%find_lang kdesnake	--with-kde
%find_lang ktron	--with-kde
%find_lang granatier	--with-kde
%find_lang kigo		--with-kde
%find_lang palapeli	--with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post			-p /sbin/ldconfig
%postun			-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
#%doc AUTHORS ChangeLog README README.highscore
%attr(755,root,root) %{_libdir}/libkdegames.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkdegames.so.?
%attr(755,root,root) %ghost %{_libdir}/libkggzgames.so.?
%attr(755,root,root) %{_libdir}/libkggzgames.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkggzmod.so.?
%attr(755,root,root) %{_libdir}/libkggzmod.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkggznet.so.?
%attr(755,root,root) %{_libdir}/libkggznet.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkmahjongglib.so.?
%attr(755,root,root) %{_libdir}/libkmahjongglib.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkolfprivate.so.?
%attr(755,root,root) %{_libdir}/libkolfprivate.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libiris_ksirk.so.?
%attr(755,root,root) %{_libdir}/libiris_ksirk.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpala.so.?
%attr(755,root,root) %{_libdir}/libpala.so.*.*.*
%{_datadir}/apps/kdegames
#%{_iconsdir}/hicolor/scalable/apps/knetwalk.svgz
#%{_iconsdir}/oxygen/scalable/actions/lastmoves.svgz
#%{_iconsdir}/oxygen/scalable/actions/legalmoves.svgz

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libkdegames.so
%attr(755,root,root) %{_libdir}/libkggzmod.so
%attr(755,root,root) %{_libdir}/libkggzgames.so
%attr(755,root,root) %{_libdir}/libkggznet.so
%attr(755,root,root) %{_libdir}/libiris_ksirk.so
%attr(755,root,root) %{_libdir}/libkolfprivate.so
%attr(755,root,root) %{_libdir}/libpala.so
%{_datadir}/apps/cmake/modules/FindLibKDEGames.cmake
%{_datadir}/apps/cmake/modules/GGZ.cmake
%dir %{_libdir}/libpala
%{_libdir}/libpala/*.cmake
%{_includedir}/*.h
%{_includedir}/digits
%{_includedir}/kgame
%{_includedir}/highscore
%{_includedir}/KDE/KCardDialog
%{_includedir}/KDE/KChat
%{_includedir}/KDE/KChatBase
%{_includedir}/KDE/KChatDialog
%{_includedir}/KDE/KExtHighscore
%{_includedir}/KDE/KGame
%{_includedir}/KDE/KGameCanvas
%{_includedir}/KDE/KGameClock
%{_includedir}/KDE/KGameDifficulty
%{_includedir}/KDE/KGameLCD
%{_includedir}/KDE/KGameMisc
%{_includedir}/KDE/KGamePopupItem
%{_includedir}/KDE/KGameProgress
%{_includedir}/KDE/KGameSvgDigits
%{_includedir}/KDE/KGameSvgDocument
%{_includedir}/KDE/KGameTheme
%{_includedir}/KDE/KGameThemeSelector
%{_includedir}/KDE/KGrid2D
%{_includedir}/KDE/KHighscore
%{_includedir}/KDE/KScoreDialog
%{_includedir}/KDE/KStandardGameAction
%{_includedir}/kggzgames
%{_includedir}/kggzmod
%{_includedir}/kggznet
%{_includedir}/Pala
%{_includedir}/libpala

%files carddecks
%defattr(644,root,root,755)
%{_datadir}/apps/carddecks

%files kdesnake
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kdesnake
%{_desktopdir}/kde4/kdesnake.desktop
%{_iconsdir}/hicolor/*x*/apps/kdesnake.png

%files ktron -f ktron.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ktron
%{_desktopdir}/kde4/ktron.desktop
%{_datadir}/apps/ktron
%{_datadir}/config.kcfg/ktron.kcfg
%{_datadir}/config/ktron.knsrc
%{_iconsdir}/hicolor/*x*/apps/ktron.png

%files bomber -f bomber.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/bomber
%{_desktopdir}/kde4/bomber.desktop
%{_datadir}/apps/bomber
%{_datadir}/config.kcfg/bomber.kcfg
%{_iconsdir}/hicolor/*x*/apps/bomber.png

%files bovo -f bovo.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/bovo
%{_desktopdir}/kde4/bovo.desktop
%{_datadir}/apps/bovo

%files kfourinline -f kfourinline.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kfourinline
%attr(755,root,root) %{_bindir}/kfourinlineproc
%{_desktopdir}/kde4/kfourinline.desktop
%{_datadir}/config.kcfg/kwin4.kcfg
%{_datadir}/apps/kfourinline
%{_iconsdir}/*/*/apps/kfourinline.png

%files katomic -f katomic.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/katomic
%{_desktopdir}/kde4/katomic.desktop
%{_datadir}/apps/katomic
%{_datadir}/config/katomic.knsrc
%{_datadir}/apps/kconf_update/katomic-levelset-upd.pl
%{_datadir}/apps/kconf_update/katomic-levelset.upd
%{_iconsdir}/*/*/apps/katomic.png

%files kiriki -f kiriki.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kiriki
%{_desktopdir}/kde4/kiriki.desktop
%{_datadir}/apps/kiriki
%{_iconsdir}/*/*/apps/kiriki.png

%files kbattleship -f kbattleship.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kbattleship
%{_desktopdir}/kde4/kbattleship.desktop
%{_datadir}/apps/kbattleship
%{_iconsdir}/*/*/apps/kbattleship.png
%{_datadir}/kde4/services/kbattleship.protocol

%files kblackbox -f kblackbox.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kblackbox
%{_desktopdir}/kde4/kblackbox.desktop
%{_datadir}/apps/kblackbox
%{_iconsdir}/*/*/apps/kblackbox.png

%files kbounce -f kbounce.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kbounce
%{_desktopdir}/kde4/kbounce.desktop
%{_datadir}/apps/kbounce
%{_iconsdir}/hicolor/*/*/kbounce.png
/var/games/kbounce.scores

%files kgoldrunner -f kgoldrunner.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kgoldrunner
%{_desktopdir}/kde4/KGoldrunner.desktop
%{_datadir}/apps/kgoldrunner
%{_datadir}/config/kgoldrunner.knsrc
%{_iconsdir}/*/*/apps/kgoldrunner.png

%files kjumpingcube -f kjumpingcube.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kjumpingcube
%{_desktopdir}/kde4/kjumpingcube.desktop
%{_datadir}/config.kcfg/kjumpingcube.kcfg
%{_datadir}/apps/kjumpingcube
%{_iconsdir}/*/*/apps/kjumpingcube.png

%files klines -f klines.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/klines
%{_desktopdir}/kde4/klines.desktop
%{_datadir}/config.kcfg/klines.kcfg
%{_datadir}/apps/klines
%{_iconsdir}/*/*/apps/klines.png

%files kmahjongg -f kmahjongg.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kmahjongg
%attr(755,root,root) %{_libdir}/libkmahjongglib.so
%{_desktopdir}/kde4/kmahjongg.desktop
%{_datadir}/apps/kmahjongg
%{_datadir}/apps/kmahjongglib
%{_datadir}/config.kcfg/kmahjongg.kcfg
%{_iconsdir}/*/*/apps/kmahjongg.png

%files kmines -f kmines.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kmines
%{_desktopdir}/kde4/kmines.desktop
%{_datadir}/apps/kmines
%{_datadir}/config/kmines.knsrc
%{_iconsdir}/*/*/apps/kmines.png

%files knetwalk
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/knetwalk
%{_desktopdir}/kde4/knetwalk.desktop
%{_datadir}/apps/knetwalk
%{_iconsdir}/*/*/apps/knetwalk.png
%{_kdedocdir}/en/knetwalk

%files kolf -f kolf.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kolf
%{_desktopdir}/kde4/kolf.desktop
%{_datadir}/apps/kolf
%{_iconsdir}/*/*/apps/kolf.png

%files konquest -f konquest.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/konquest
%{_desktopdir}/kde4/konquest.desktop
%{_datadir}/apps/konquest
%{_iconsdir}/*/*/apps/konquest.png

%files kpat -f kpat.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kpat
%{_desktopdir}/kde4/kpat.desktop
%{_datadir}/apps/kpat
%{_datadir}/apps/kconf_update/kpat_update_cardwidth.upd
%{_iconsdir}/*/*/apps/kpat.png

%files kreversi -f kreversi.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kreversi
%{_desktopdir}/kde4/kreversi.desktop
%{_datadir}/apps/kreversi
%{_iconsdir}/*/*/actions/legalmoves.png
%{_iconsdir}/*/*/actions/lastmoves.png
%{_iconsdir}/*/*/apps/kreversi.png

%files ksame -f ksame.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ksame
%{_desktopdir}/kde4/ksame.desktop
%{_datadir}/apps/ksame
%{_iconsdir}/*/*/apps/ksame.png

%files kshisen -f kshisen.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kshisen
%{_desktopdir}/kde4/kshisen.desktop
%{_datadir}/config.kcfg/kshisen.kcfg
%{_datadir}/apps/kshisen
%{_datadir}/sounds/kshisen
%{_iconsdir}/*/*/apps/kshisen.png

%files ksquares -f ksquares.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ksquares
%{_desktopdir}/kde4/ksquares.desktop
%{_datadir}/config.kcfg/ksquares.kcfg
%{_datadir}/apps/ksquares
%{_iconsdir}/*/*/apps/ksquares.png

%files ksudoku -f ksudoku.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ksudoku
%{_desktopdir}/kde4/ksudoku.desktop
%{_datadir}/apps/ksudoku
%{_datadir}/config/ksudokurc
%{_iconsdir}/*/*/apps/ksudoku.png

%files kspaceduel -f kspaceduel.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kspaceduel
%{_desktopdir}/kde4/kspaceduel.desktop
%{_datadir}/apps/kspaceduel
%{_datadir}/config.kcfg/kspaceduel.kcfg
%{_iconsdir}/*/*/apps/kspaceduel.png

%files ktuberling -f ktuberling.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ktuberling
%{_desktopdir}/kde4/ktuberling.desktop
%{_datadir}/apps/ktuberling
%{_iconsdir}/*/*/apps/ktuberling.png

%files lskat -f lskat.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/lskat
%{_desktopdir}/kde4/lskat.desktop
%{_datadir}/apps/lskat
%{_iconsdir}/*/*/apps/lskat.png


%files kblocks -f kblocks.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kblocks
%{_desktopdir}/kde4/kblocks.desktop
%{_datadir}/apps/kblocks
%{_datadir}/config.kcfg/kblocks.kcfg
%{_datadir}/config/kblocks.knsrc
%{_iconsdir}/*/*/apps/kblocks.png

%files kbreakout -f kbreakout.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kbreakout
%{_desktopdir}/kde4/kbreakout.desktop
%{_datadir}/apps/kbreakout
%{_iconsdir}/*/*/apps/kbreakout.png

%files kdiamond -f kdiamond.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kdiamond
%{_desktopdir}/kde4/kdiamond.desktop
%{_datadir}/apps/kdiamond
%{_datadir}/config/kdiamond.knsrc
%{_iconsdir}/*/*/apps/kdiamond.png
#%{_iconsdir}/hicolor/scalable/apps/kdiamond.svgz
%{_datadir}/sounds/KDiamond-Stone-Drop.ogg
%{_datadir}/sounds/KDiamond-Stone-Swap.ogg
%{_datadir}/sounds/KDiamond-Stone-Touch.ogg

%files kollision -f kollision.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kollision
%{_desktopdir}/kde4/kollision.desktop
%{_datadir}/apps/kollision
%{_iconsdir}/*/*/apps/kollision.png
#%{_iconsdir}/oxygen/scalable/apps/kollision.svgz

%files ksirk -f ksirk.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ksirk
%attr(755,root,root) %{_bindir}/ksirkskineditor
%{_desktopdir}/kde4/ksirk.desktop
%{_datadir}/apps/ksirk
%{_datadir}/config.kcfg/ksirksettings.kcfg
%{_iconsdir}/*/*/apps/ksirk.png
%{_desktopdir}/kde4/ksirkskineditor.desktop
%{_datadir}/apps/ksirkskineditor
%{_datadir}/config.kcfg/ksirkskineditorsettings.kcfg
%{_datadir}/config/ksirk.knsrc
%{_kdedocdir}/en

%files kubrick -f kubrick.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kubrick
%{_desktopdir}/kde4/kubrick.desktop
%{_datadir}/apps/kubrick
%{_iconsdir}/*/*/apps/kubrick.png

%files kapman -f kapman.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kapman
%{_desktopdir}/kde4/kapman.desktop
%{_datadir}/apps/kapman
%{_datadir}/sounds/kapman
%{_iconsdir}/*/*/apps/kapman.png
#%{_iconsdir}/hicolor/scalable/apps/kapman.svgz

%files killbots -f killbots.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/killbots
%{_desktopdir}/kde4/killbots.desktop
%{_datadir}/config.kcfg/killbots.kcfg
%{_datadir}/apps/killbots
%{_iconsdir}/*/*/apps/killbots.png

%files granatier -f granatier.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/granatier
%{_datadir}/apps/granatier
%{_datadir}/applications/kde4/granatier.desktop
%{_datadir}/config.kcfg/granatier.kcfg
%{_iconsdir}/hicolor/*x*/apps/granatier.png

%files kigo -f kigo.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kigo
%{_datadir}/apps/kigo
%{_datadir}/applications/kde4/kigo.desktop
%{_datadir}/config.kcfg/kigo.kcfg
%{_datadir}/config/kigo-games.knsrc
%{_datadir}/config/kigo.knsrc
%{_iconsdir}/hicolor/*x*/apps/kigo.png

%files palapeli -f palapeli.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/palapeli
%attr(755,root,root) %{_bindir}/libpala-puzzlebuilder
%attr(755,root,root) %{_libdir}/kde4/palapeli_jigsawslicer.so
%attr(755,root,root) %{_libdir}/kde4/palapeli_rectslicer.so
%attr(755,root,root) %{_libdir}/kde4/palathumbcreator.so
%{_datadir}/apps/palapeli
%{_datadir}/kde4/services/ServiceMenus/palapeli_servicemenu.desktop
%{_datadir}/kde4/services/palapeli_jigsawslicer.desktop
%{_datadir}/kde4/services/palapeli_rectslicer.desktop
%{_datadir}/kde4/services/palathumbcreator.desktop
%{_datadir}/kde4/servicetypes/libpala-slicerplugin.desktop
%{_datadir}/mime/packages/palapeli-mimetypes.xml
%{_datadir}/applications/kde4/palapeli.desktop
%{_datadir}/config/palapeli-collectionrc
