#include <iostream>

using std::cout;
using std::cin;
using std::endl;
using std::ostream;

class Fraction
{
private:
    int nu;
    int deno;
public:
    Fraction(int num = 1, int de = 1)
    {
        if (0 != de)
        {
            this->nu = num;
            this->deno = de;    
        }
        else
            cout << "Failed, denominator cannot be 0!" << endl;
    }

    Fraction operator+(const Fraction &frac2)
    {
        int num = this->nu * frac2.deno + frac2.nu * this->deno;
        int de = this->deno * frac2.deno;
        return Fraction(num, de);
    }

    Fraction operator-(const Fraction &frac2)
    {
        int num = this->nu * frac2.deno - frac2.nu * this->deno;
        int de = this->deno * frac2.deno;
        return Fraction(num, de);
    }

    Fraction operator*(const Fraction &frac2)
    {
        int num = this->nu * frac2.nu;
        int de = this->deno * frac2.deno;
        return Fraction(num, de);
    }

    Fraction operator/(const Fraction &frac2)
    {
        int num = this->nu * frac2.deno;
        int de = this->deno * frac2.nu;
        if (0 == de)
            exit(-1);
        else
            return Fraction(num, de);
    }

    bool operator==(const Fraction & frac2)
    {
        if ((this->nu * frac2.deno) == (this->deno * frac2.nu))
            return true;
        else
            return false;
    }

    Fraction operator=(const Fraction& frac2)
    {
        Fraction newFrac(frac2.nu, frac2.deno);
        return newFrac;
    }


    friend ostream & operator << (ostream &os, Fraction & frac)
    {
        os << frac.nu << " / " << frac.deno;
        return os;
    }

    void setValue(int num, int de)
    {
        this->nu = num;
        this->deno = de;
    }
};

int main()
{
    Fraction frac1 = Fraction(1, 2);
    Fraction frac2 = Fraction(1, 3);
    Fraction frac3 = frac1 + frac2;
    Fraction frac4 = frac3;
    cout << frac3 << endl;
    cout << &frac1 << '\n' << &frac2 << '\n' << &frac3 << endl;
    cout << &frac4 << endl;
    frac4 = frac3;
    cout << &frac3 << endl;
    cout << &frac4 << endl;
    frac4.setValue(1, 4);
    cout << frac3 << '\n' << frac4 << endl;
}