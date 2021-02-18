#include <iostream>
using namespace std;

class contohclass {         
  public:               
    void hello() {   
      cout << "Hello World!";
    }
};

int main() {
  contohclass objectclass;    
  objectclass.hello();  
  return 0;
}
