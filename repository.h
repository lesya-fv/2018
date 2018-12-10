#pragma once
#include<iostream>
#include<list>
#include<string>
#include<fstream>
#include"Shelf.h"
#include"hash.h"
#include <algorithm>

struct Repository
{
	std::list<std::string>* repository;
	void insert(std::string bookname);
	void destroy(std::string bookname);
	void find(std::string bookname);
    Repository();
    ~Repository();
};

Repository::Repository()
{
    repository = new std::list<std::string>[1000000];
}


Repository::~Repository()
{
    delete[] repository;
}

void Repository::insert(std::string bookname)
{
	int index = (int)abs(generetichash(bookname)%1000000);
	std::cout << index << std::endl;
	repository[index].push_back(bookname);
}

void Repository::destroy(std::string bookname)
{
	int index = (int)abs(generetichash(bookname) % 1000000);
    auto list = repository[index];
    
    auto it = std::find(repository[index].begin(), repository[index].end(), bookname);
    if (it == repository[index].end())
        return;
    list.erase(it);
}

void Repository::find(std::string bookname)
{
	int index = (int)abs(generetichash(bookname) % 1000000);
    
    auto it = std::find(repository[index].begin(), repository[index].end(), bookname);
    if (it == repository[index].end())
        std::cout << bookname << " -- this book not exist" << std::endl;
    else
        std::cout << bookname << " -- this book does exist" << std::endl;        
}


/*void Repository::readfile(std::string filename)
{
	std::ifstream tmp_file(filename);
	std::string tmp_str = "";
	while (tmp_file)
	{
		std::string str;
		std::getline(tmp_file, str);
		if (str != "")
		{
			Repository::insert(str);
		}

	}
}*/
