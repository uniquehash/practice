



#ifndef SPACEOBJECT_H
#define SPACEOBJECT_H

class SpaceObject					
{

public:
	SpaceObject(int, int);			// initializes the x and y position of any object
	void	update();				// increments the y position of the object

	vec2i	getPos() const;			// returns the position of the object
	void	setPos(vec2i);			

private:
	vec2i	pos;
};

class ObjectField
{

public:
	void	update();							// erases objects that are out of bounds anc calls SpaceObjects::update to change the y position of the remaining objects
	void	erase(size_t);						// removes object from vector at index i
	std::vector<SpaceObject> getData() const;	// returns the vector containing our objects
	void	setBounds(rect);					// sets boundary of our objects to variable a

private:
	rect	field_bounds;
	std::vector<SpaceObject> object_set;
};

#endif






















