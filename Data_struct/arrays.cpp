#include <iostream>
//  Implement a vector (mutable array with automatic resizing):
//  Practice coding using arrays and pointers, and pointer math to jump to an index instead of using indexing.
// using namespace std;

class array{
  private:
    int size;
    int* newArr;
    int capacity;

  public:
    array(){
      size=0;
      capacity=16;
      newArr= new int[16];
    }

    int at(int in){
      return newArr[in];
    }

    void insert(int index,int num){
      if(index<0||index>size){
        cout<<"wrong index";
      }
      // for (int i = 0; i < size; i++) {
      //   if (i == index+1) {
      //     push(num);
      //   }
      //   push(pop());
      // }
      // size++;

      int* arr=new int[size];
      for(int i =index,j=0;i<size;j++,i++){
        arr[j]=newArr[i];
      }
      newArr[index] = num;
      size++;
      for (int i = index +1,j=0;i<size;j++,i++){
        newArr[i]=arr[j];
      }
      delete [] arr;
      arr=NULL;
    }

    void prepend(int num) {
      insert(0,num);
    }

    int find(int num){
      for (int i =0; i<size ; i++){
        if (newArr[i]==num){
          return i;
        }
      }
      return -1;
    }



    void remove(int num){
      for(int i = 0; i<size; i++){
        if(newArr[i]==num){
          deleteNum(i);
        }
      }
    }

    void deleteNum(int index){
      if(index<0||index>size){
        cout<<"wrong index"<<endl;
      }

      int* temp = new int[size];
      for (int i = index, j = 0; i < size; i++, j++) {
        temp[j] = newArr[i];

      }

      temp++;
      size--;

      for (int j = index, i = 0; j < size; j++, i++) {
        newArr[j] = temp[i];
      }

    }

    int pop(){
      int val = newArr[0];
      newArr++;
      size--;
      if(size ==capacity/4){
      resize(size/2);
    }
      return val;
    }

    bool is_empty(){
      if(size==0){
        return true;
     }
      return false;
    }

    void push(int num){
      if (size==capacity){
        resize(size*2);
      }
      newArr[size]=num;
      size++;
    }

    int getCapacity(){
      return capacity;
    }

    int getSize(){
      return size;
    }

    void out(){
      for (int i = 0; i < size; i++) {
        std::cout << newArr[i] << "  ";
      }
    }
  private:
    void resize(int newCap){
        int* newArr2 = new int[newCap];
        capacity=newCap;
        for(int i =0;i<size;i++){
          newArr2[i]=newArr[i];
        }
        delete [] newArr;
        newArr=newArr2;
        newArr2 = NULL;
    }


};

int main(){
  array newArr;
  for (int i = 0; i < 20; i++) {
    newArr.push(i);
  }

  newArr.out();
  cout<<newArr.find(588888);
  newArr.out();


  return 0;

}
