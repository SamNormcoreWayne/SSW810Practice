#include <iostream>
#include <algorithm>
#include <unordered_map>
#include <vector>
#include <string>
#include <random>

using std::cout;
using std::endl;
using std::cin;
using std::default_random_engine;
using std::uniform_int_distribution;
using std::vector;
using std::unordered_map;
using std::string;

char get_answer()
{
    vector<char> answer = {'R', 'P', 'S'};
    std::random_device sed;
    std::mt19937 rand(sed());
    uniform_int_distribution<unsigned> domain(0, 2);
    return answer[domain(rand)];
}

int main()
{
    unordered_map<char, unordered_map<char, string>>  result = {{'R', {{'R', "Tie"}, {'S', "Win"}, {'P', "Lose"}}}, {'P', {{'P', "Tie"}, {'S', "Lose"}, {'R', "Win"}}}, {'S', {{'S', "Tie"}, {'P', "Win"}, {'R', "Lose"}}}};

    while (true)
    {
        char human;
        cout << "Please choose 'R', 'P', 'S' or 'Q' to quit. " << endl;
        cin >> human;
        char computer;
        computer = get_answer();

        if (tolower(human) == 'q')
        {
            cout << "Thx for playing" << endl;
            break;
        }
        else
            cout << result[toupper(human)][computer] << endl;
    }
}