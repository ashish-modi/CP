#include<iostream>
#include<vector>

using namespace std;

void display(vector<int> &v)
{
    vector<int>::iterator iter1;
    cout << endl;

    for(iter1 = v.begin(); iter1 != v.end() ; iter1++)
        cout << *iter1 << " ";
}

int main()
{
    vector<int> v1;    // didn't specify the number of elements so it will create an empty vector      
    //vector<int>::iterator iter;  // creating an iterator for vector which is just like a pointer 


    for(int i=0 ; i<=5; i++)
        v1.push_back(i);
/*    
    cout << "Vector v1: "<< endl;

    for(iter= v1.begin() ; iter != v1.end() ; iter++)
        cout << *iter << " " ;                // using de-referencing operator for fetching value 
     
    // another way of displaying the elements of vector is using "auto"

    cout << endl << "USING AUTO KEYWORD "<< endl;
    for(auto iter1 = v1.begin(); iter1 != v1.end(); iter1++)
        cout << *iter1 << " ";
    
    // accesing by element using iter2 iterator
    
    cout << endl << "Accessing by element " << endl;
    for(auto iter2:v1)
        cout << iter2 << " ";     // here iter2 is treated as element 


    cout << "Size of vector v1 : " << v1.size() << endl;
    for(int i = 0 ; i != v1.size() ; i++)
        cout << v1[i] << " ";

    v1.pop_back();

    cout << "After using pop_back the size of the vector is : " << v1.size();



    display(v1);

    // fixing the size of vector makes sapces in the array initialized with 0

    vector<int> v3(12);       
    cout << "Size of vector : " << v3.size();
    v3[9] = 9;
    display(v3);

*/


    // it is an array of initially empty vectors to which you can add elements.
    // It is just like 2D matrix

    vector<int> v2[4]; 

    v2[1].push_back(10);
    v2[1].push_back(12);
    v2[2].push_back(20);
    v2[3].push_back(30);
    v2[0].push_back(40);

    cout << "Size of 2D matrix : " << sizeof(v2);
    for(int i= 0 ; i < 4 ; i++)
        display(v2[i]);
 
    
    return 0;
}