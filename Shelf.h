#pragma once
#include<string>
#include"hash.h"

struct Shelf
{
	std::string bookname;
	Shelf(std::string name)
	{
		this->bookname = name;
	}
}; 
