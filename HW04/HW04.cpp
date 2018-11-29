#include <iostream>
#include <unordered_map>
#include <algorithm>
#include <cctype>

using std::cout;
using std::cin;
using std::endl;
using std::unordered_map;
using std::string;

string toLower(string str)
{
    string tmp = str;
    for(auto i = 0; i < tmp.size() && isupper(tmp[i]); ++i)
        tmp[i] = tolower(tmp[i]);
    return tmp;
}

int count_vowels(string str)
{
    int count = 0;
    string tmp = str;
    tmp = toLower(tmp);
    cout << tmp << endl;
    for (auto i : tmp)
    {
        switch (i)
        {
            case 'a':
            case 'e':
            case 'i':
            case 'o':
            case 'u':
                count++;
                break;
        }
    }

    return count;
}

string Search(string target, string str)
{
    string tmp = toLower(str);
    for (int i = tmp.size(); i > 0; --i)
    {
        if target == tmp[i]
            return i;
    }
    return string("end");
}

int main()
{
    string str = "HEllo, world";

    cout << count_vowels(str) << endl;
}