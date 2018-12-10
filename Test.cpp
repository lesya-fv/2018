#include <iostream>
#include "repository.h"

void readfile(Repository* r, std::string filename)
{
    std::ifstream tmp_file(filename);
	std::string tmp_str = "";
	while (tmp_file)
	{
		std::string str;
		std::getline(tmp_file, str);
		if (str != "")
		{
			r->insert(str);
		}

	}
}

int main()
{
    Repository r;
    readfile(&r, "bookslist.txt");
    r.insert("The Hunger Games");
    r.find("The Hunger Games");

	return 0;
} 
