#pragma once
#include <string>
#include <math.h>



int generetichash(std::string bookname)
{
	long long int hash = 0;
	long long int mark = 0;
	for (int i = 0; i < bookname.length(); i++)
	{
		mark = sqrt((int)(bookname[i]));
		mark = (int)mark;
		mark = (mark + 56) - (int)(bookname[i]) % 10;
		mark = pow((mark), 4);
		hash += mark;

	}

	return hash;
}
