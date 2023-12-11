// #include<bits/stdc++.h>
// using namespace std;
// class node{
//     public:
//     int data;
//     node* next;
//     node* prev;
//     // node(){
//     //     data=0;
//     //     next=NULL;
//     //     prev=NULL;
//     // }
//     node(int val){
//         data=val;
//         next=NULL;
//         prev=NULL;
//     }
// };
// class binary{
//     private:
//     node* head;
//     node* tail;
//     public:
//     binary(){
//         head=NULL;
//         tail=NULL;
//     }
//     void insert(int val){
//         node* p=new node(val);
//         if(head==NULL) {
//             head=tail=p;
//         }
//         else{
//            p->prev=tail;
//            tail->next=p;
//            tail=p;
//         }
        
        
//     }
//     void display(){
//         node*temp=head;
//         while(temp!=NULL){
//             cout<<temp->data;
//             temp=temp->next;
//         }
//     }

// };
// int main(){
//     binary obj;
//     obj.insert(1);
//     obj.insert(0);
//     obj.insert(1);
//     obj.insert(0);
//     obj.display();
//     cout<<endl;
//     cout<<"once's compliment = ";
//     obj.one();
//     obj.display();
//     cout<<endl;
//     cout<<"two's compliment = ";
//     obj.two();
//     obj.display();
// }