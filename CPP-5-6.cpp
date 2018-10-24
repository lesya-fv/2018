#include <iostream> 
#include <string>


template<class type>
struct Node // храним значения и адрес (узел)
{
    type value;
    Node<type>* next;
    Node(type value, Node* next)
    {
        this->value = value; // переходим по указателю
        this->next = next;
    }
    
};

template<class type>
struct list // обращаемся по адресу самого первого элемента
{
    Node<type>* head = 0; // <=> nullptr
    int l_size = 0;
    void push_front(type value);
    void push_back(type value);
    void elem_del(int index);
    void clear();
    void go_to_print();
};

template<class type>
void list<type>::push_front(type value) // функция из list
{
    head = new Node<type>(value, head); // new создает указатели
}

template<class type>
void list<type>::push_back(type value)
{
    Node<type>* current = head; // с ним проходим list
    if (head == 0)
        head = new Node<type>(value, head);
    else 
    {
        for (int i = 0; i < l_size-1; i++)
        {
            current = current -> next;
        }
        current -> next = new Node<type>(value, 0);
    }
    l_size++;
}

template<class type>
void list<type>::elem_del(int index) // очищаем значение, а потом ссылку удаляем
{
    if (index <= l_size - 1)
    {
        if (index == 0)
        {
            Node<type>* tmp_head = head -> next; // создаем кандидата на следующую голову
            delete head;
            head = nullptr;
            head = tmp_head;
        
        } else if (index == l_size - 1) 
        {
            Node<type> *current = head;
            for (int i = 0; i < l_size - 2; i++) 
            {
                current = current->next;
            }
            delete current->next;
            current->next = nullptr;
        }
         else 
        {
            Node<type>* prev_elem;
            Node<type>* next_elem;
            Node<type>* current = head;
            for (int i = 0; i <= index; i++)
            {
                if (1 == index-i)
                    prev_elem = current;
                if (i == index )
                {                    
                    next_elem = current->next;
                    delete current;
                    current = nullptr;
                    break;
                }
                current = current->next;                
            }
            prev_elem->next = next_elem;            
        }
        l_size--;
    }
}

template<class type>
void list<type>::clear()
{
    for (int i = 0; i < l_size; i++)
        elem_del(0);
}

template<class type>
void list<type>::go_to_print()
{
    Node<type> *tmp = head;
    for (int i = 0; i < l_size-1; i++)
    {
        std::cout << tmp -> value << std::endl;
        tmp = tmp -> next;
    }
    std::cout << tmp -> value << std::endl;
}

int main()
{
    list<double> listick;
}
