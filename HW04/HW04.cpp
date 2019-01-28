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
    for(auto i = tmp.begin(); i != tmp.end() && isupper(*i); ++i)     
        *i = tolower(*i);
    return tmp;
}

int count_vowels(string str)
{
    int count = 0;
    string tmp = str;
    tmp = toLower(tmp);
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

string Search(char target, string str)
{
    string tmp = toLower(str);
    target = (char)tolower(target);
    for (int i = tmp.size(); i > 0; --i)
    {
        if (target == tmp[i])
            return std::to_string(i + 1);
    }
    return string("end");
}

int main()
{
    string str = "HEllo, world";

    cout << count_vowels(str) << endl;
    cout << Search('o', str) << endl;
}