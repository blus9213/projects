#include<iostream>
#include<string.h>
using namespace std;

class  apple{
    int val;
public:
     apple(){
        val =1;
    }
    apple(int x){
        val= x;
    }
    int get(){
        return val;
    }
    apple operator + (apple a){
        apple temp;
        temp.val = val + a.val;
        return temp;
        }
};





int main(){
apple a;
apple b(2);
 apple sum = a +b;
 cout<< sum.get()<<endl;



}