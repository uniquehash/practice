#include <unistd.h>
#include <ncurses.h>

#include <cstdlib>
#include <cstdint>
#include <string>
#include <vector>

#include "game.h"
#include "ObjectField.h"

WINDOW* main_wnd;
WINDOW*	game_wnd;

rect	game_area;
rect	screen_area;

vec2ui	cur_size;

ObjectField asteroids;
ObjectField stars;

struct
{
	vec2i	pos;
	rect	bounds;
	char	disp_char;
	int		energy;
} player;

int	init()
{
	srand(time(0));							// seeding rand
	main_wnd = initscr();					// ncurses init
	cbreak();
	noecho();
	clear();
	refresh();
		
	curs_set(0);
	start_color();
	screen_area = { {0, 0}, {80, 50}};		// default terminal size, (x, y) format

	int	infopanel_height = 4;
	game_wnd = newwin(	screen_area.height() - infopanel_height - 2,	// defining the bounds of our 
						screen_area.width() - 2,						// two windows using newwin
						screen_area.top() + 1,							
						screen_area.left() + 1);							
	main_wnd = newwin(	screen_area.height(), screen_area.width(), 0, 0);	
	game_area = {{0, 0}, { static_cast<uint_fast16_t>(screen_area.width() - 2), static_cast<uint_fast16_t>(screen_area.height() - infopanel_height - 4)}};

	init_pair(1, COLOR_WHITE, COLOR_BLACK);		// useful color pairs
	init_pair(2, COLOR_GREEN, COLOR_BLACK);
	init_pair(3, COLOR_YELLOW, COLOR_BLACK);
	init_pair(4, COLOR_RED, COLOR_BLACK);
	init_pair(5, COLOR_BLUE, COLOR_BLACK);

	keypad(main_wnd, true);		// enable function keys
	keypad(game_wnd, true);

	nodelay(main_wnd, true);	// disable input blocking
	nodelay(game_wnd, true);

	return 0;
}

void	run()
{
	// refactoring for sanity
	int		tick;
	
	player.disp_char = '0';
	player.pos = {10, 5};

	asteroids.setBounds(game_area);		// constrains objects to game area
	stars.setBounds(game_area);

	int		in_char = 0;
	bool	exit_requested = false;
	bool	game_over = false;
	
	// draw outlines of the defined windows, screen consists of a fram around the edge and a horizontal
	// dividing line near the bottom. divides screen into game area and score area
	wattron(main_wnd, A_BOLD);						
	box(main_wnd, 0, 0);								// draw frame around whole screen
	wattroff(main_wnd, A_BOLD);

	wmove(main_wnd, game_area.bot() + 3, 1);			// draw dividing line between game and stats
	whline(main_wnd, '-', screen_area.width() - 2);

	wrefresh(main_wnd);		//initial draw
	wrefresh(game_wnd);

	// we can clear game screen every execution (more performent)
	tick = 0;
	while(1)
	{
		werase(game_wnd);				// clear game window

		in_char	= wgetch(main_wnd);		// read inputs
		in_char = tolower(in_char);		// lowercase all characters
		
		switch(in_char)
		{
			case 'q':
				exit_requested = true;
				break;
			case KEY_UP:
			case 'w':
			case 'i':
				if(player.pos.y < game_area.top())			// player bounds checking
					player.pos.y -= 1;
				break;
			case KEY_DOWN:
			case 's':
			case 'k':
				if(player.pos.y < game_area.bot() + 1)		// player bounds checking
					player.pos.y += 1;
				break;
			case KEY_LEFT:
			case 'a':
			case 'j':
				if(player.pos.x > game_area.left() + 1)		// player bounds checking
					player.pos.x -= 1;
				break;
			case KEY_RIGHT:
			case 'd':
			case 'l':
				if(player.pos.x < game_area.right() - 2)	// player bounds checking
					player.pos.x += 1;
				break;
			default:
				break;
		}

		// update stars position 
		if (tick % 7 == 0)
			stars.update();

		// update asteroids position
		if (tick > 100 && tick % 20 == 0)
			asteroids.update();

		// the players hit box
		player.bounds = {{static_cast<uint_fast16_t>(player.pos.x -1), static_cast<uint_fast16_t>(player.pos.y)}, {3, 1}};	// player is 3x1

		// asteroid, player hit detection
		for(size_t i = 0; i < asteroids.getData().size(); i++)
		{
			if (player.bounds.contains(asteroids.getData().at(i).getPos()))
			{
				asteroids.erase(i);
			}
		}

		// draw stars
		for (auto s: stars.getData())
			mvwaddch(game_wnd, s.getPos().y, s.getPos().x, '.');	

		// draw asteroids
		for (auto a: asteroids.getData())
		{
			wattron(game_wnd, A_BOLD);
			mvwaddch(game_wnd, a.getPos().y, a.getPos().x, '*');
			wattroff(game_wnd, A_BOLD);
		}


		// draw the character and refresh each window, perform tick + sleep
		// mvwaddch differs from mvaddch in that it takes the window as first attribute
		wattron(game_wnd, A_BOLD);
		mvwaddch(game_wnd, player.pos.y, player.pos.x, player.disp_char);	// draw the player body
		wattroff(game_wnd, A_BOLD);

		// improved spaceship draw
		wattron(game_wnd, A_ALTCHARSET);
		mvwaddch(game_wnd, player.pos.y, player.pos.x -1, ACS_LARROW);
		mvwaddch(game_wnd, player.pos.y, player.pos.x +1, ACS_RARROW);

		// add engine flame
		if ((tick % 10) / 3)
		{
			wattron(game_wnd, COLOR_PAIR(tick % 2 ? 3 : 4));
			mvwaddch(game_wnd, player.pos.y + 1, player.pos.x, ACS_UARROW);
			wattroff(game_wnd, COLOR_PAIR(tick % 2 ? 3 : 4));
		}

		wattroff(game_wnd, A_ALTCHARSET);

		wrefresh(main_wnd);
		wrefresh(game_wnd);

		if (exit_requested || game_over) break;

		tick++;

		usleep(10000); // 10ms

	}

}

void	close()
{
	endwin();
}





































