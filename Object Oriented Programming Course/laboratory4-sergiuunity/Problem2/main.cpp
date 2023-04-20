#include "BigInteger.h"
#include "bigint_test.h"

#include <iomanip>
#include <iostream>
using namespace std;


BigInteger computeNthFibonacci(BigInteger n) {
    BigInteger a = BigInteger("1");
    BigInteger b = BigInteger("1"); 
    BigInteger c = BigInteger("1"); 
    if (n.sgn()==0)
        return c;
    n--;
    while (n.sgn() != 0) {
        c = a + b;
        b = a;
        a = c;
        n--;
    }
    return b;
}


int main() {
#if ENABLE_TESTS > 0
	run_bigint_tests(true);
#endif
 /*   FIBONACCI OVERFLOW
    long long int crt = -1;
    long long int prev = -1;
    bool isOverflow = false;
    for (int n = 0; n < 100; n+=10) {
        prev = crt;
        crt = computeNthFibonacci(n);
        if (crt < prev)
            isOverflow = true;
        cout << setw(5) << n << "\t" << setw(70)<<crt<<"\t"<<(isOverflow ? string(RED)+string("OVERFLOW !!!! ")+string(NC) : "") << endl;

    }*/

    BigInteger crt("-1");
    BigInteger prev("-1");
    bool isOverflow = false;
    for (BigInteger n = BigInteger("0"); n < BigInteger("100"); n+=BigInteger("10")) {
        prev = crt;
        crt = computeNthFibonacci(n);
        if (crt < prev)
            isOverflow = true;
        cout << setw(5) << n << "\t" << setw(70)<<crt<<"\t"<<(isOverflow ? string(RED)+string("OVERFLOW !!!! ")+string(NC) : "") << endl;

    }


    return 0;
}