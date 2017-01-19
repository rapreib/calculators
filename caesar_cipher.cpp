/*
  NAME:     Rebecca A Preib
  DATE:     01/19/2017
  PROJECT:  Caesar Cipher: Encrypt and Decrypt
*/

#include <iostream>
#include <string>
#include <cctype>

bool get_enc_info(char &enc_or_dec, int &key, std::string &text);

int main()
{
  char enc_or_dec = 'Q';
  int key = 0;
  std::string text = "";
  bool run_alg = get_enc_info(enc_or_dec, key, text);

  std::cout << run_alg << " " << enc_or_dec << " " << key << " " << text << "\n";

  while (run_alg) {
    switch(enc_or_dec) {
      // Encrypt Algorithm
      case 'e': 
        for (int counter = 0; counter < text.length(); counter++) {
          if (text[counter] != ' ') {
            char a = (text[counter] + key);
            std::cout << a;
          }
        }
        break;

      // Decrypt Algorithm
      case 'd':
        for (int counter = 0; counter < text.length(); counter++) {
          if (text[counter] != ' ') {
            char a = (text[counter] - key);
            std::cout << a;
          }
        }
        break;

      default:
        std::cout << "Please enter E to encrypt, D to decrypt, or Q to quit";
        break;
    } // end switch
    std::cout << "\n";
    run_alg = get_enc_info(enc_or_dec, key, text);
  } // end while

  std::cout << "Goodbye!\n";
  return 0;
}

bool get_enc_info(char &enc_or_dec, int &key, std::string &text) {
  std::cout << "Encrypt or Decrypt? (enter E, D, or Q) ";
  std::cin >> enc_or_dec;
  enc_or_dec = tolower(enc_or_dec);
  if(enc_or_dec == 'q') {
    return false;
  }

  std::cout << "Enter key: ";
  std::cin >> key;
  std::cout << "Enter text: ";
  // read in the end of the 'key' line
  getline(std::cin, text); 
  getline(std::cin, text);
  return true;
}

