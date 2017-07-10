#include <unistd.h>
#include <ncurses.h>

#include <cstdlib>
#include <cstdint>
#include <string>
#include <vector>

#include "game.h"
#include "ObjectField.h"

WINDOW* wnd;

struct
{
	vec2i	pos;
	char	disp_char;
} player;			

ObjectField stars;

int	init()
{
	wnd = initscr();
	cbreak();
	noecho();
	clear();
	refresh();
	
	keypad(wnd, true); 	
	nodelay(wnd, true); 
	curs_set(0);		
	
	if (!has_colors())	
	{
		endwin();
		printf("ERROR: Terminal does not support color.\n");
		exit(1);
	}
	else
		start_color();		
	
	attron(A_BOLD);			
	box(wnd, 0, 0);			
	attroff(A_BOLD);

	init_pair(1, COLOR_WHITE, COLOR_BLACK);
	wbkgd(wnd, COLOR_PAIR(1));

	return 0;
}

void	run()
{
	int	in_char;	
	bool	exit_requested = false;

	player.disp_char = '0';
	player.pos = {10, 5};
	
	uint_fast16_t maxY, maxX;					// these will be used to initialize rect
	getmaxyx(wnd, maxY, maxX);					// get window boundaries

	rect game_area = { {0, 0}, {maxX, maxY}};	// initialize our rect with 0 offset
	stars.setBounds(game_area);					// set our star bounds

	while(1)
	{
		in_char = wgetch(wnd);
		stars.update();
		
		for(auto s : stars.getData())					// this removes each object from it's previous position
		{												// on the screen by replacing it with a space on the screen
			mvaddch(s.getPos().y, s.getPos().x, ' ');	// instead. this will be replaced by a more efficient method
		}													
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

		for(auto s : stars.getData())					// use getPos() to get position of stars
		{												// displays given character at given position
			mvaddch(s.getPos().y, s.getPos().x, '*');	// on game window
		}
		mvaddch(player.pos.y, player.pos.x, player.disp_char);
		
		refresh();
		if(exit_requested) break;
		usleep(10000);
	}
}

void	close()
{
	endwin();
}





































