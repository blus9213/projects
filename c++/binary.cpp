#include<iostream>
#include<string.h>
using namespace std;

struct node{
    int a ;
    node *left = NULL;
    node *right = NULL;
    
};
node *add(int c){
    node* ptr1 = new node;
    ptr1->a = c;
    ptr1->left = NULL;
    ptr1->right= NULL;
    return ptr1;

};
void taver(node*ptr,int f){// traversal using DFS preorder and targer is F
    if (ptr == NULL){
        cout<<"not found"<<endl;
        return;
    }
    else{
    if(ptr->a==f) {
        cout<<"found"<<endl;
        return;}
    taver(ptr->left,f);
    taver(ptr->right,f);

}
}
int main(){
    node *root = add(1);
    root->left = add(2);
    root->right = add(3);
    taver(root,5);
    cin.get();
}

