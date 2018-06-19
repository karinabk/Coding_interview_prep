#include <iostream>
#include <vector>
using namespace std;

int binary_search(std::vector<int> v,int num){
  int lo=0, hi=v.size()-1;
  while(lo<=hi){
    int mid = lo+(hi-lo)/2;
    if(num==v[mid]){
      return mid;
    }
    if(num>v[mid]){
      lo=mid+1;
    }
    if(num<v[mid]){
      hi=mid-1;
    }
  }
  return -1;
}

int binary_search_recursion(std::vector<int> v,int hi, int lo, int num){
  
  int mid = lo+(hi-lo)/2;
  if(v[mid]==num){
    return mid;
  }
  if(lo>hi){
    return -1;
  }
  if(num>v[mid]){
    return binary_search_recursion(v,hi,mid+1,num);
  }
  if(num<v[mid]){
    return binary_search_recursion(v,mid-1,lo,num);
  }
}


int main(){

  std::vector<int> v(15) ;
  for(int i = 0;i<14;i++){
    
    v[i]=i*3;
    std::cout<<"Value: "<< i*3<<"Index: "<< i<<endl;
  }
  
  std::cout <<"binary search "<<binary_search(v,6) << '\n';
  std::cout<<"binary recursion "<<binary_search_recursion(v, 15,1,6)<< '\n';

}
