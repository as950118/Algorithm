#include <iostream>
#include <stdio.h>
using namespace std;
int RGB[3], n, r, g, b;
enum { R, G, B };
int main() {
    cin >> n;
    for (int i = 0; i < n; i++) {
        int ir = RGB[R], ig = RGB[G], ib = RGB[B];
        cout<<ir<<" "<<ig<<" "<<ib<<" "<<endl;
        cin >> r >> g >> b;
        RGB[R] = r + min(ig, ib);
        RGB[G] = g + min(ir, ib);
        RGB[B] = b + min(ir, ig);
    }
    cout << min(RGB[R], min(RGB[G], RGB[B])) << endl;
    return 0;
}

