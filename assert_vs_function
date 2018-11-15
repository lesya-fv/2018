#include <iostream>
#include <math.h>
#include <cassert>

void is_equal(int value1, int value2)
{
    if (value1 == value2)
        std::cout << "value1 and value2 are equal (true)" << std::endl;
    else
        std::cout << "value1 and value2 are different (false)" << std::endl;
}

void is_not_equal(int value1, int value2)
{
    if (value1 == value2)
        std::cout << "value1 and value2 are equal (false)" << std::endl;
    else
        std::cout << "value1 and value2 are different (true)" << std::endl;
}

void is_equal_0(int value)
{
    if (value == 0)
        std::cout << "value is equal to 0 (true)" << std::endl;
    else
        std::cout << "value is not equal to 0 (false)" << std::endl;
}

void is_not_equal_0(int value)
{
    if (value != 0)
        std::cout << "value is not equal to 0 (true)" << std::endl;
    else
        std::cout << "value is equal to 0 (false)" << std::endl;
}

#define ASSERT_EQUAL(value1, value2) assert(value1 == value2); std::cout << "value1 and value2 are equal" << std::endl
#define ASSERT_NEQUAL(value1, value2) assert(value1 != value2); std::cout << "value1 and value2 are different" << std::endl
#define ASSERT_TRUE(value) assert(value == 0); std::cout << "value is equal to 0" << std::endl
#define ASSERT_FALSE(value) assert(value != 0); std::cout << "value is not equal to 0" << std::endl

int print()
{
    std::cout << "enter the value" << std::endl;
    int value;
    std::cin >> value;
    return value;
}

int main()
{
    std::cout << "Enter:" << std::endl;
    std::cout << "1 to check ASSERT_EQUAL" << std::endl;
    std::cout << "2 to check ASSERT_NEQUAL" << std::endl;
    std::cout << "3 to check ASSERT_TRUE" << std::endl;
    std::cout << "4 to check ASSERT_FALSE" << std::endl;
    std::cout << "5 to check is_equal function" << std::endl;
    std::cout << "6 to check is_not_equal function" << std::endl;
    std::cout << "7 to check is_equal_0 function" << std::endl;
    std::cout << "8 to check is_not_equal_0 function" << std::endl;    
    int count = 0;
    std::cin >> count;
    switch (count)
    {
    case 1:
        {
        int value1 = print();
        int value2 = print();
        ASSERT_EQUAL(value1, value2);
        break;
        }
    case 2:
        {
        int value1 = print();
        int value2 = print();
        ASSERT_NEQUAL(value1, value2);
        break;
        }
    case 3:
        {
        int value1 = print();
        ASSERT_TRUE(value1);
        break;
        }
    case 4:
        {
        int value1 = print();
        ASSERT_FALSE(value1);
        break;
        }
    case 5:
        {
        int value1 = print();
        int value2 = print();
        is_equal(value1, value2);
        break;
        }
    case 6:
        {
        int value1 = print();
        int value2 = print();
        is_not_equal(value1, value2);
        break;
        }
    case 7:
        {
        int value1 = print();
        is_equal_0(value1);
        break;
        }
    case 8:
        {
        int value1 = print();
        is_not_equal_0(value1);
        break;
        }
    default:
        std::cout << " incorrect data " << std::endl;
    }
    return 0;
    return 0;
}
