#include <iostream>
#include <stdio.h>
#include <math.h>
#include <string>
#include <fstream> 
#include <iomanip> 
#include <cstring>
#include <vector>           
#include <sstream>          
#include <algorithm>     
#include <cassert>
#include <iostream>
#include <string>

class hash

{

private:
    static const int table_size = 3;
    
    struct book
    {
        std::string title;
        std::string author;
        book* next;
    };
    
    book* HashTable[table_size];

public:
    int Hash(std::string key);
    void AddItem(std::string title, std::string author);
    int NumberOfBooksInIndex(int index);
    void BookInfo();

};

int hash::Hash(std::string key)

{   
    for (int i = 0; i < table_size; i++)
    {
        HashTable[i] = new book;
        HashTable[i] -> title = "empty";
        HashTable[i] -> author = "empty";
        HashTable[i] -> next = NULL;
    }
    
    int hash_i = 0;
    
    for (int i = 0; i < key.length(); i++)
    {
        hash_i = hash_i + (int)key[i];
    }
    
    int index = hash_i % (table_size);

    return index;

}

void hash::AddItem(std::string title, std::string author)
{
    int index = Hash(title);
    
    if (HashTable[index] -> title == "empty")
    {
        HashTable[index] -> title = title;
        HashTable[index] -> author = author;
        std::cout << title << " 7" << std::endl;
    }
    else
    {
        book* ptr = HashTable[index];
        book* n = new book;
        n -> title = title;
        n -> author = author;
        n -> next = NULL;
        while (ptr -> next != NULL)
        {
            ptr = ptr -> next;
        }
        ptr -> next = n;
        std::cout << title << " " << author << std::endl;
    }
}

int hash::NumberOfBooksInIndex(int index)
{
    int count = 0;
    if (HashTable[index] -> title == "empty")
        return count;
    else
    {
        count++;
        book* ptr = HashTable[index];
        while (ptr -> next != NULL)
        {
            count++;
            ptr = ptr -> next;
        }
    }
}

void hash::BookInfo()
{
    std::cout << table_size << std::endl;
    int number;
    for (int i = 0; i < table_size; i++)
    {
        number = NumberOfBooksInIndex(i);
        std::cout << " " << std::endl;
        std::cout << "index = " << i << std::endl;
        std::cout << HashTable[i] -> title << std::endl;
        std::cout << HashTable[i] -> author << std::endl;
        std::cout << "number of books = " << number << std::endl;
        std::cout << " " << std::endl;
    }
}

int main(int argc, char** argv)

{
    hash hashy;
    hashy.Hash("initial");

    hashy.BookInfo();
    
    return 0;

}
 
