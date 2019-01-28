#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>

using std::fstream;
using std::string;
using std::vector;

auto strip(string str)
{
    /*
     * Why C++ does not have a strip function!
     */
    vector<char> strV;
    // Using a linear container would be eaiser to delete, and add elements.
    std::stringstream ss;
    for (auto i = str.begin(); i != str.end(); ++i)
    //auto = std::string::iterator
        if (*i != '\r' && *i != '\n')
            strV.push_back(*i);
    for (auto i = strV.begin(); i != strV.end(); ++i)
    //auto = std::string::iterator
        ss << (char)*i;

    return ss.str();
}

auto strToVector(string str)
{
    vector<char> strV;
    for (auto i = str.begin(); i != str.end(); ++i)
    {
        //auto = std::string::iterator
        strV.push_back(*i);
    }
    return strV;
}

auto vectorToStr(vector<char> strV)
{
    std::stringstream ss;
    for (auto i = strV.begin(); i != strV.end(); ++i)
    //auto = std::string::iterator
        ss << *i;
    return ss.str();
}

auto getLine(string filePath)
{
    fstream fp;
    fp.open(filePath, std::fstream::in | std::fstream::out);
    if (!fp.is_open())
    {
        std::cout << "Cannot open" + filePath << std::endl;
        exit(-1);
    }
    string line;
    vector<string> lines;
    while (std::getline(fp, line))
    {
        line = strip(line);
        vector<char> lineV = strToVector(line);
        if (lineV.empty())
            continue;
        // I do not want to see empty lines!
        while (lineV.back() == '\\')
        {
            // delete commments here
            lineV.pop_back();
            std::getline(fp, line);
            line = vectorToStr(lineV) + strip(line);
            lineV = strToVector(line);
        }

        vector<char>::iterator i;
        // I will need this i after the loop finished
        for (i = lineV.begin(); i != lineV.end() && *i != '#'; ++i)
            ;
        vector<char> tmp(lineV.begin(), i);
        if (!tmp.empty())
            lines.push_back(vectorToStr(tmp));
    }
    fp.close();
    return lines;
}

int main()
{
    string path = "C:\\Users\\64937\\OneDrive\\Documents\\SSW\\810\\HW05\\test.txt";
    vector<string> lines = getLine(path);
    for (auto i = lines.begin(); i != lines.end(); ++i)
    // auto ==  std::vector<string>::iterator
        std::cout << *i << std::endl;
}