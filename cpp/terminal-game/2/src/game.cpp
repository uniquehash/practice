#include <cstdlib>
#include <string>
#include <ncurses.h>
#include <unistd.h>

#include "game.h"

WINDOW* wnd;

struct				// a simple player, has a position and a char to represent itself
{
	vec2i	pos;
	char	disp_char;
} player;			

int	init()
{
	wnd = initscr();
	cbreak();
	noecho();
	clear();
	refresh();
	
	keypad(wnd, true); 	// enables ncurses to interpret action keys rather than print out escape sequences
	nodelay(wnd, true); 	// disables blocking when using `wgetch()` it's important to animate while listening to input
	curs_set(0);		// tells ncurses to make the cursor invisible
	
	if (!has_colors())	// lets us know whether or not the terminal supports color manipulation
	{
		endwin();
		printf("ERROR: Terminal does not support color.\n");
		exit(1);
	}
	else
		start_color();		// enables routines that let you redefine colors within a terminal
	
	attron(A_BOLD);			// used to activate an attribute for drawing (this case bold type)
	box(wnd, 0, 0);			// draws a box around the edges of a window
	attroff(A_BOLD);

	init_pair(1, COLOR_WHITE, COLOR_BLACK);	// takes two colors and assigns them to a number, number is passed into COLOR_PAIR macro
	wbkgd(wnd, COLOR_PAIR(1));		// wbkgd changes the forground and background based on the COLOR_PAIR it received

	return 0;
}

void	run()
{
	int	in_char;	
	bool	exit_requested = false;

	player.disp_char = '0';		// assign the players character rep
	player.pos = {10, 5};		// assign the players position
	
	while(1)
	{
		in_char = wgetch(wnd);

		mvaddch(player.pos.y, player.pos.x, ' ');
		switch(in_char)
		{
			case 'q':
				exit_requested = true;
				break;
			case KEY_UP:
			case 'w':
				player.pos.y -= 1;
				break;
			case KEY_DOWN:
			case 's':
				player.pos.y += 1;
				break;
			case KEY_LEFT:
			case 'a':
				player.pos.x -= 1;
				break;
			case KEY_RIGHT:
			case 'd':
				player.pos.x += 1;
				break;
			default:
				break;

		}
		mvaddch(player.pos.y, player.pos.x, player.disp_char);	// draws the player
		refresh();
		if(exit_requested) break;
	}
}

void	close()
{
	endwin();
}





































