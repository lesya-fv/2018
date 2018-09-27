#include <iostream>
#include <string>

class Patient
{
    private:
        std::string name, surname, town;
        int id, age, visits_number;
    public:
        void add_new_person (int set_id, std::string set_name, std::string set_surname, std::string set_town, int set_age)
        {
            id = set_id;
            name = set_name;
            surname = set_surname;
            town = set_town;
            age = set_age;
            visits_number = 0;
        }
        
        void get_persons_characteristics ()
        {
            std::cout << "ID: " << id << "; name: " << name << "; surname: " << surname << "; town: " << town << "; age: " << age << "; number of visits: " << visits_number << std::endl;    
        }
        
        void visits (int number)
        {
            visits_number += number;
        }
};

Patient db[5];

void add_visits ()
{
    std::cout << "Enter person`s ID " << std::endl;
    int t, q;
    std::cin >> t;
    std::cout << "Enter the number of visits you want to add " << std::endl;
    std::cin >> q;
    db[t-1].visits (q);
}

// Функция info не работает
void info ()
    {
    int new_size = sizeof(db)/sizeof(db[0])+1;
    Patient help_db[new_size];
    int k = 0;
    for (k = 0; k < new_size; k++)
        {
        help_db[k] = db[k]; // Вот здесь что-то пошло не так
        }
    std::cout << "Enter person`s name, surname, town, age " << std::endl;
    std::string add_name, add_surname, add_town;
    int add_age;
    std::cin >> add_name >> add_surname >> add_town >> add_age;
    help_db[new_size].add_new_person (new_size, add_name, add_surname, add_town, add_age);
    std::cout << "The information about " << add_name << " " << add_surname << " has been written" << std::endl;
    help_db[new_size].get_persons_characteristics ();
    }

int main()
{
    std::string names_towns[5][3] = {{"Leo", "Tolstoy", "Tula"},
                                     {"Fedor", "Dostoevsky", "Moscow"},
                                     {"Ivan", "Turgenev", "Orel"},
                                     {"Anton", "Chekhov", "Taganrog"},
                                     {"Mikhail", "Lermontov", "Moscow"}};
    int age[5] = {13, 20, 23, 19, 27};
    int i = 0;
    for (i = 0; i <= 4; i++)
        {
        db[i].add_new_person (i+1, names_towns[i][0], names_towns[i][1], names_towns[i][2], age[i]);
        }
    std::cout << "Enter: '1' to get information about a patient; '2' to add a patient; '3' to add visits " << std::endl;
    int count = 0;
    std::cin >> count;
    switch (count)
    {
    case 1:
        {
        std::cout << "Enter ID " << std::endl;
        int w = 0;
        std::cin >> w;
        db[w-1].get_persons_characteristics ();
        break;
        }
    case 2:
        {
        info();
        break;
        }
    case 3:
        {
        add_visits ();
        break;
        }
    default:
        std::cout << " I`m just a stupid programm, I don`t understand what you mean " << std::endl;
    }
    return 0;
